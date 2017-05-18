{
    "architectures": [
        "SCMP_ARCH_X86_64"
    ],
    "defaultAction": "SCMP_ACT_ERRNO",
    "syscalls": [
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "brk"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "rt_sigaction"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "unlinkat"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "listen"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "setgroups"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "lseek"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "wait4"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "getsockname"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "accept"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [
                {
                    "index": 0,
                    "op": "SCMP_CMP_EQ",
                    "value": 1,
                    "valueTwo": 0
                },
                {
                    "index": 1,
                    "op": "SCMP_CMP_EQ",
                    "value": 526337,
                    "valueTwo": 0
                }
            ],
            "name": "socket"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [
                {
                    "index": 0,
                    "op": "SCMP_CMP_EQ",
                    "value": 16,
                    "valueTwo": 0
                },
                {
                    "index": 1,
                    "op": "SCMP_CMP_EQ",
                    "value": 3,
                    "valueTwo": 0
                }
            ],
            "name": "socket"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [
                {
                    "index": 0,
                    "op": "SCMP_CMP_EQ",
                    "value": 2,
                    "valueTwo": 0
                },
                {
                    "index": 1,
                    "op": "SCMP_CMP_EQ",
                    "value": 524289,
                    "valueTwo": 0
                }
            ],
            "name": "socket"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [
                {
                    "index": 0,
                    "op": "SCMP_CMP_EQ",
                    "value": 10,
                    "valueTwo": 0
                },
                {
                    "index": 1,
                    "op": "SCMP_CMP_EQ",
                    "value": 524289,
                    "valueTwo": 0
                }
            ],
            "name": "socket"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "exit_group"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "gettimeofday"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "munmap"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "epoll_create1"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [
                {
                    "index": 1,
                    "op": "SCMP_CMP_MASKED_EQ",
                    "value": 0,
                    "valueTwo": 4294967290
                }
            ],
            "name": "access"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "setgid"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "epoll_ctl"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "mprotect"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "stat"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "set_tid_address"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "times"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "exit"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "open"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "getppid"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "sendto"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "connect"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "clone"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "pipe"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "epoll_wait"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "futex"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "geteuid"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "fcntl"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "getcwd"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "newfstatat"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "setuid"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "uname"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "madvise"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "arch_prctl"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "select"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "close"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "ioctl"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "getrlimit"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "fstat"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "rt_sigprocmask"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [
                {
                    "index": 0,
                    "op": "SCMP_CMP_LE",
                    "value": 16,
                    "valueTwo": 0
                },
                {
                    "index": 2,
                    "op": "SCMP_CMP_LE",
                    "value": 8192,
                    "valueTwo": 0
                }
            ],
            "name": "read"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "set_robust_list"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "writev"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "mmap"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "procexit"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "bind"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "recvmsg"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "execve"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "signaldeliver"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "getpid"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "sigreturn"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "dup"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "shutdown"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "setsockopt"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "openat"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "clock_gettime"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "getdents64"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "lstat"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "capget"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "prctl"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "getgid"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "fchown"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "getuid"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "capset"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "chdir"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "rt_sigreturn"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "write"
        },
        {
            "action": "SCMP_ACT_ALLOW",
            "args": [],
            "name": "dup3"
        }
    ]
}