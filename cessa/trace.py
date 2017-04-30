# encoding: utf-8

"""
cessa.trace
===========

This module implements container class and corresponding methods for tracing containers.

:Copyright (c) by hac(Xiao An) <hac@zju.edu.cn>. All Rights Reserved.

"""

import subprocess
import docker
import os.path
import logging

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

    def run(self, with_seccomp=False):
        """ runs container

        :with_seccomp: whether to use seccomp profile
        :returns: Popen object

        """
        cmd = ['docker', 'run']
        if with_seccomp and self.seccomp != None:
            cmd += ['--security-opt', 'seccomp={}'.format(self.seccomp)]
        cmd += ['--name', self.name]
        if self.opts != None:
            cmd += self.opts
        cmd.append(self.image_id)
        p = subprocess.Popen(cmd,
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE,
                             universal_newlines = True)
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

def trace(container, trace_file):
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
        container.kill()
    except Exception as e:
        print(logging.exception(e))
        raise RuntimeError('Unable to trace container \'{}\''.format(container.name))





