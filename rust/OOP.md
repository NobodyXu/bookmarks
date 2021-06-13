 1. [Object Oriented Programming Features of Rust](https://doc.rust-lang.org/book/ch17-00-oop.html)

## inheritance

 1. [How to implement inheritance-like feature for rust?](https://users.rust-lang.org/t/how-to-implement-inheritance-like-feature-for-rust/31159/21)
    
    TL;DR:
    
    Instead of using object is of type `Base`, use object as type `Base` by defining function `fn as_base(&self) -> &Base`.
    
    Using composite is considered to be better than inheritance (which indeed have many problems) in rust.
