 1. [Notes on Inlining](https://numba.pydata.org/numba-doc/latest/developer/inlining.html)
    
    TL;DR:
    
    numba's `inline = always` option in `jit` (or `njit`) is not for performance but for type inference.
    
    Optimization is done by llvm and by default numba uses `-O3`.
