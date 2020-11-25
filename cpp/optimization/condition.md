 1. [How branches influence the performance of your code and what can you do about it?](https://johnysswlab.com/how-branches-influence-the-performance-of-your-code-and-what-can-you-do-about-it/)
 2. [Bit Twiddling Hacks - branchless algorithms](https://graphics.stanford.edu/~seander/bithacks.html)
 3. [Make your programs run faster: avoid function calls](https://johnysswlab.com/make-your-programs-run-faster-avoid-function-calls/)
    
    TIPs:
     - `__attribute__((flatten))` for inlining function calls in this function is possible.
     - ` __attribute__((pure))` for functions only depends on input arguments and state of the memory (content of the pointers) and cannot
       modify memory.
     - `__attribute__((const))` for functions only depends on input arguments (not pointer dereferences).
     - `void * __attribute__((noinline)) get_pc () { return _builtin_return_address(0); }`
