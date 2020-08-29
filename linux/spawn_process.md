## `posix_spawn`: safer `vfork()` + `exec()` and portable

 1. [Intro to `posix_spawn`](https://zatrazz.github.io/Launching-Process/)
 2. According to source code of `posix_spawn`, it fixes:
    - Allocate a stack for child by `mmap`.
    - Blocks all signal except the unblockable in parent before vforking.
    - Disable asynchronous cancellation in parent.
    - Users can config `posix_spawn` to reset all signal handler to default in child.
    - Users can config `posix_spawn` to set signal mask to the desired value in child.
    
    But it does have one drawback: If signal handler isn't reset or signal mask isn't set to ignore all, then `posix_spawn` will
    recover parents' signal mask before `execve`, creating a possible race condition thus open up a possible way to hack the child.
