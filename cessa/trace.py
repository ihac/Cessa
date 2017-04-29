# encoding: utf-8

"""
cessa.trace
===========

This module implements container class and corresponding methods for tracing containers.

:Copyright (c) by hac(Xiao An) <hac@zju.edu.cn>. All Rights Reserved.

"""

import subprocess
import docker

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
        :returns: None

        """
        cmd = ['docker', 'run']
        if with_seccomp and self.seccomp != None:
            cmd += ['--security-opt', 'seccomp={}'.format(self.seccomp)]
        cmd += ['--name', self.name]
        if self.opts != None:
            cmd += self.opts
        cmd.append(self.image_id)
        p = subprocess.run(cmd,
                           stdout = subprocess.PIPE,
                           stderr = subprocess.PIPE,
                           universal_newlines = True)
        if p.returncode != 0:
            raise RuntimeError('Unable to run container {} with command \'{}\''.format(self.name, cmd), p.stderr)

    def exec_workload(self):
        """TODO: Docstring for exec_workload.
        :returns: TODO

        """
        pass

    def kill(self):
        """TODO: Docstring for kill.
        :returns: TODO

        """
        pass


def trace(container):
    """TODO: Docstring for trace.

    :container: TODO
    :returns: TODO

    """
    pass
