 1. [primitive type - never](https://doc.rust-lang.org/nightly/std/primitive.never.html)
 2. [crate - fixed point float](https://docs.rs/fixed/1.9.0/fixed/)
    
    [crate - fixed_sqrt](https://docs.rs/fixed-sqrt/0.2.4/fixed_sqrt/)
    
    [crate - cordic](https://docs.rs/cordic/0.1.5/cordic/)
 3. [crate- bytemuck](https://docs.rs/bytemuck/1.6.1/bytemuck/index.html)
 4. [Exotically sized types](https://doc.rust-lang.org/nomicon/exotic-sizes.html)


## operater overloading
 1. [How do I make a struct callable?](https://stackoverflow.com/questions/42859330/how-do-i-make-a-struct-callable)
    
    TL;DR:
    
    Can't do it in stable Rust as of Jun, 2021, but it can be simulated with the `Deref` trait to return a lambda.


## Interior Mutability
 1. [Interior Mutability - The Rust Reference](https://doc.rust-lang.org/reference/interior-mutability.html)
    
    TL;DR:
    
    Use [`std::cell::UnsafeCell`](https://doc.rust-lang.org/std/cell/struct.UnsafeCell.html)
