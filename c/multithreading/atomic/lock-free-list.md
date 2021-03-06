 1. [Simple lock free stack c++11]
 
## ABA problem
 1. [ABA problem, Wikipedia]
 
 Solution to it:
 
 1. [Read-copy-update, Wikipedia]
 2. [What is RCU, Fundanmentally?]
 3. [Linux Restartable Sequences](https://www.efficios.com/blog/2019/02/08/linux-restartable-sequences/)
    
    [compudj/librseq](https://github.com/compudj/librseq)
    
    [compudj/librseq man page](https://github.com/compudj/librseq/blob/master/doc/man/rseq.2)
    
    [torvalds/linux/kernel/rseq.c](https://github.com/torvalds/linux/blob/master/kernel/rseq.c)
    
    TL;DR:
    
    This allows situations where:
     - The thread is migrated to another CPU
     - A signal is delivered to the thread
     - The thread is preempted
    to be detected by the thread and quickly restart the critical section.
    
    **Only one critical section per thread can be active at any time**.
    
    **Restartable sequences must not perform system calls. Doing so may result in termination of the process by a segmentation fault.**
    
    **Limitation: if you single-step through a critical section in the debugger, the program will loop forever.**
    
    `rsq()` can speedup CPU id retrieving, thus speedup access of per-cpu data.
    
    It can also benefit atomic data structure as it makes the CPU scheduler transparent to the process.
    
    For example, when implementing delete operation for an atomic container, how do you ensure others won't visit the already deleted data?
    <br>Using atomic counter that frees the data when it reached 0 won't fix the problemm since some threads might be preempted and later resumed after 
    the data is freed.
    <br>Using `rsq` + atomic counter fixes this problem, as any thread that preempts can be reset to the previous data it is visiting.
    <br>This is appliable to atomic list and atomic hashmap.
    
 4. [Userspace RCU](https://liburcu.org/)

[Simple lock free stack c++11]: https://stackoverflow.com/questions/26747265/simple-lock-free-stack-c11
[ABA problem, Wikipedia]: https://en.wikipedia.org/wiki/ABA_problem
[Read-copy-update, Wikipedia]: https://en.wikipedia.org/wiki/Read-copy-update
[What is RCU, Fundanmentally?]: https://lwn.net/Articles/262464/
