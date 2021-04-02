 1. [Simple lock free stack c++11]
 
## ABA problem
 1. [ABA problem, Wikipedia]
 
 Solution to it:
 
 1. [Read-copy-update, Wikipedia]
 2. [What is RCU, Fundanmentally?]
 3. [Linux Restartable Sequences](https://www.efficios.com/blog/2019/02/08/linux-restartable-sequences/)
    [compudj/librseq](https://github.com/compudj/librseq)
    
    TL;DR:
    
    This allows situations where:
     - The thread is migrated to another CPU
     - A signal is delivered to the thread
     - The thread is preempted
    to be detected by the thread and quickly restart the critical section.
    
    **Only one critical section per thread can be active at any time**.
    
    **Limitation: if you single-step through a critical section in the debugger, the program will loop forever.**
    
    `rsq()` can speedup CPU id retrieving, thus speedup access of per-cpu data.
    
    It can also benefit atomic data structure as it makes the CPU scheduler transparent to the process.

[Simple lock free stack c++11]: https://stackoverflow.com/questions/26747265/simple-lock-free-stack-c11
[ABA problem, Wikipedia]: https://en.wikipedia.org/wiki/ABA_problem
[Read-copy-update, Wikipedia]: https://en.wikipedia.org/wiki/Read-copy-update
[What is RCU, Fundanmentally?]: https://lwn.net/Articles/262464/
