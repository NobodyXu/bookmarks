 1. [Why are Rust executables so huge?](https://stackoverflow.com/questions/29008127/why-are-rust-executables-so-huge)
    
    TL;DR:
    
    It's because rust's standard library are statically linked with the executable by default.
    
    Add:
    
    ```
    [build]
    rustflags = ['-C', 'prefer-dynamic']
    ```
    
    to `<your cargo project>/.cargo/config.toml` (or `~/.cargo/config.toml` for all projects build on your computer) to make it generate a dynamic library and the size of rust
    will be comparable to C/C++.
    
 2. [johnthagen/min-sized-rust](https://github.com/johnthagen/min-sized-rust)
    
    Many methods in this list does not work with the point 1.
