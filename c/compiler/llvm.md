 1. [polly](https://polyhedral.info/)
    
    > - Program analysis
    >    - Dependence analysis
    >    - Array expansion and single assignment transformation
    >    - Liveness and reuse/locality analysis of array elements
    >    - Array region analysis and approximations
    >    - Scheduling theory
    > 
    > - Farkas lemma and multi-dimensional scheduling
    >    - Automatic vectorization and parallelization of nested loops
    >    - Link with loop transformations (interchange, fusion, retiming, etc.)
    >    - Loop tiling and tiling models
    >    - Program verification
    > 
    > - Computability and decidability
    >    - Program termination
    >    - Race detections
    >    - Mapping algorithms
    > 
    > - Systolic array design
    >    - Memory mapping with memory reuse (array contraction)
    >    - Data mapping (HPF-like), data distribution for distributed memory
    >    - Communication optimizations
    >    - Counting and Ehrhart polynomials
    > 
    > - Analysis of cache misses
    >    - Memory size computations
    >    - Iteration counting (WCET)
    >    - Parallelizing compiler developments
    > 
    > - Hardware synthesis
    >    - Automatic vectorizers/parallelizers
    >    - Compilation for GPUs
    >    - Iterative compilation
    >    - Binary optimizations and runtime optimizations
 2. [Using Polly with Clang](https://bcain-llvm.readthedocs.io/projects/polly/en/latest/UsingPollyWithClang/)
    
    TL;DR:
    
    Basic usage:
    
    ```
    # Polly requires optimization in -O3 to work
    clang -O3 -mllvm -polly file.c
    ```
    
    To enable automatic OpenMP code generation, add `-mllvm -polly-parallel -lgomp` to command above.
    
    To enable vector code generation, add `-mllvm -polly-vectorizer=stripmine` to command above.
