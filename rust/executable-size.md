 1. [Why are Rust executables so huge?](https://stackoverflow.com/questions/29008127/why-are-rust-executables-so-huge)
    
    TL;DR:
    
    It's because rust's standard library are statically linked with the executable by default.
    
    Add:
    
    ```
    [build]
    rustflags = ['-C', 'prefer-dynamic']
    ```
    
    to `<your cargo project>/.cargo/config.toml` to make it generate a dynamic library and the size of rust
    will be comparable to C/C++.
