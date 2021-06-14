 1. [Porting a C++ Program to Rust: Of reinterpret_cast, Structs and Bluetooth](https://stackoverflow.com/questions/42418964/porting-a-c-program-to-rust-of-reinterpret-cast-structs-and-bluetooth)
    
    TL;DR:
    
    Just use `unsafe std::mem::transmute` or pointer to do it.
    <br>There's no strict aliasing in rust.
