## `posix_spawn`: safer `vfork()` + `exec()` and portable

 1. [Intro to `posix_spawn`](https://zatrazz.github.io/Launching-Process/)
 2. According to source code of `posix_spawn`, it fixes:
    - Allocate a stack for child by `mmap`.
    - Blocks all signal except the unblockable in parent before vforking.
    - Disable asynchronous cancellation in parent.
    - In child process, `posix_spawn` will set some of the signal handler to either `SIG_DFL` or `SIG_IGN`.
