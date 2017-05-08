# !/usr/bin/env python3
# encoding: utf-8

"""
cessa.trace
===========

This module implements container class and corresponding methods for tracing containers.

:Copyright (c) by hac(Xiao An) <hac@zju.edu.cn>. All Rights Reserved.

"""

import subprocess
import os.path
import logging
import shutil
import re
from os import makedirs
from time import sleep
from cessa import docker

import json
SYSDIG_CONF_FILE = 'expert/sysdig.json'

class Container(object):

    """ Stores key info for a container to be traced, particularly, workload scripts.

    """

    def __init__(self, name, image_id):
        container_id = docker.query_container(name)
        if container_id != None:
            raise ValueError('Conflict. The contianer name {} is already in use by container {}'.format(name, container_id))
        self.name = name
        if docker.query_image(image_id) == None:
            raise ValueError('Unable to find image {} locally'.format(image_id))
        self.image_id = image_id

        self.opts = []
        self.workload = None
        self.seccomp = None

    def set_option(self, opts):
        """ sets options for running container without checking their correctness!

        :opts: options
        :returns: None
        """
        self.opts += opts

    def set_workload(self, script_file):
        """ sets workload script for testing container.

        :script_file: EXECUTABLE workload script file(absolute path)
        :returns: None

        """
        if os.path.isfile(script_file):
            raise RuntimeError('Workload script \'{}\' not exists'.format(script_file))
        self.workload = script_file

    def set_seccomp(self, profile):
        """ sets seccomp profile for limiting container.

        :profile: seccomp profile(path)
        :returns: None

        """
        if os.path.isfile(profile):
            raise ValueError('Seccomp profile \'{}\' not exists'.format(profile))
        self.seccomp = profile

    def run(self, with_seccomp=False):
        """ runs container

        :with_seccomp: whether to use seccomp profile
        :returns: Popen object

        """
        cmd = ['docker', 'run']
        if with_seccomp and self.seccomp != None:
            cmd += ['--security-opt', 'seccomp={}'.format(self.seccomp)]
        cmd += ['--name', self.name]
        if len(self.opts) != 0:
            cmd += self.opts
        cmd.append(self.image_id)
        p = subprocess.Popen(cmd,
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE,
                             universal_newlines = True)
        sleep(0.1)
        if None != p.poll() > 0:
            _, err = p.communicate()
            raise RuntimeError('Unable to run container {} with command \'{}\''.format(self.name, cmd), err)
        return p

    def exec_workload(self):
        """ execute the workload script of container
        :returns: None

        """
        if self.workload == None:
            raise RuntimeError('No workload script specified for container \'{}\''.format(self.name))
        if os.path.isfile(self.workload):
            raise RuntimeError('Workload script \'{}\' not exists'.format(self.workload))
        cmd = [self.workload]
        p = subprocess.Popen(cmd,
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE,
                             universal_newlines = True)
        returncode = p.wait()
        _, err = p.communicate()
        if returncode != 0:
            raise RuntimeError('Failed to run workload script \'{}\''.format(self.workload), err)

    def remove(self, force=True):
        """ removes container
        :returns: None

        """
        cmd = ['docker', 'rm']
        if force: cmd.append('-f')
        cmd.append(self.name)
        p = subprocess.run(cmd,
                           stdout = subprocess.PIPE,
                           stderr = subprocess.PIPE,
                           universal_newlines = True)
        if p.returncode != 0:
            raise RuntimeError('Unable to remove container {} with command \'{}\''.format(self.name, cmd), p.stderr)

def start_sysdig(container_name, out_fp):
    """ starts sysdig to trace syscalls.

    :container_name: container name
    :out_fp: file object for storing traced syscalls
    :returns: Popen object

    """
    cmd = ['sysdig', 'container.name = {}'.format(container_name), 'and', 'syscall.type exists']
    p = subprocess.Popen(cmd,
                         stdout = out_fp,
                         stderr = subprocess.PIPE,
                         universal_newlines = True)
    if None != p.poll() > 0:
        _, err = p.communicate()
        raise RuntimeError('Unable to start sysdig with command \'{}\''.format(cmd), err)
    return p

def trace_syscall(container, trace_file):
    """ uses sysdig to trace container's syscall with executing workload script.

    :container: container to be traced
    :trace_file: file path for storing traced syscalls
    :returns: None

    """
    # two exceptions here: start_sysdig error and open_file error. Catch them!
    try:
        sysdigp = start_sysdig(container.name, open(trace_file, 'w'))
        container.run()
        container.exec_workload()
        sysdigp.kill()
        container.remove()
    except Exception as e:
        print(logging.exception(e))
        raise RuntimeError('Unable to trace container \'{}\''.format(container.name))

def data_preprocessing(trace_file, out_dir='.'):
    """ preprocesses trace file and separates syscall records by sort-uniq

    :trace_file: file with syscall trace
    :out_dir: output directory for separated syscall records
    :returns: syscall list

    """
    if not os.path.isdir(out_dir):
        raise ValueError('\'{}\' is not a directory'.format(out_dir))
    syscall_info = {}
    syscall_list = set()
    try:
        sysdig_conf = load_sysdig_conf()
        for line in open(trace_file, 'r'):
            mark, name, *args = line.split()[5:]
            # '>' means syscall entry, '<' means syscall return
            if mark == '>':
                name, _ = correct_syscall(name, None, sysdig_conf)
                syscall_list.add(name)
                if syscall_info.get(name, None) == None:
                    syscall_info[name] = [args]
                else:
                    syscall_info[name].append(args)
        # dump into file
        # then, sort and uniq
        for name, args_list in syscall_info.items():
            syscall_dir = os.path.join(out_dir, name)
            syscall_file = os.path.join(syscall_dir, 'args.list')
            if os.path.exists(syscall_dir):
                shutil.rmtree(syscall_dir)
            makedirs(syscall_dir)
            with open(syscall_file, 'w') as fp:
                for args in args_list:
                    if len(args) != 0: fp.write('{}\n'.format(' '.join(args)))

            syscall_uniq_file = os.path.join(syscall_dir, 'args.uniq.list')
            cmd = ['sort {} | uniq -c | sort -nr > {}'.format(syscall_file, syscall_uniq_file)]
            p = subprocess.run(cmd,
                               shell = True,
                               stdout = subprocess.PIPE,
                               stderr = subprocess.PIPE,
                               universal_newlines = True)
            if p.returncode != 0:
                raise RuntimeError('Unable to sort syscall records with command \'{}\''.format(cmd))
    except Exception as e:
        raise e
    return syscall_list


def retrieve_arg_value(syscall, arg_record_file):
    """ retrieves argument values from a preprocessed record file

    :syscall: the name of system call
    :arg_record_file: output file of data_preprocessing()
    :returns: dictionary with key=combination of syscall name and arg name, value=set of arg value

    """
    arg_value_dict = {}
    sysdig_conf = load_sysdig_conf()
    for line in open(arg_record_file, 'r'):
        _, *arg_list = line.split()
        for arg in arg_list:
            p = re.match("(\w+)=(\d+).*", arg)
            if p == None:
                continue
            arg_name, arg_value = syscall+'_'+p.group(1), int(p.group(2))
            _, arg_name = correct_syscall(syscall, arg_name, sysdig_conf)
            if arg_value_dict.get(arg_name, None) == None:
                arg_value_dict[arg_name] = {arg_value}
            else:
                arg_value_dict[arg_name].add(arg_value)
    return arg_value_dict

def load_sysdig_conf():
    """ loads sysdig config into json object

    :returns: JSON object

    """
    return json.load(open(SYSDIG_CONF_FILE, 'r'))

def correct_syscall(syscall, arg, conf):
    """ corrects syscall name and argument name
    This method makes sense because sysdig produces syscall/argument names which are conflicting with linux man page.

    :syscall: syscall name
    :arg: argument name
    :returns: correct syscall and correct arg

    """
    if conf['correct'].get(syscall, None) == None:
        return syscall, arg
    syscall_conf = conf['correct'][syscall]
    syscall = syscall_conf['name']

    if arg == None or syscall_conf['arguments'].get(arg, None) == None:
        return syscall, arg
    return syscall, syscall_conf['arguments'][arg]
