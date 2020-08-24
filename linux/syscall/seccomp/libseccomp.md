 1. [handle multiplexed syscall](https://www.spinics.net/lists/linux-security-module/msg35312.html)
 
    Just use `SCMP_SYS` or `seccomp_syscall_resolve_name_arch` to resolve syscall name, it should be fine.
