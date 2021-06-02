 1. [non type parameters in generics](https://www.google.com/amp/s/amp.reddit.com/r/rust/comments/jy95xq/what_are_const_generics/)
    
    Supported

 2. Varadic generic: Not supported directly, but can be emulated using macro (print! for example is implemented using macro)
 3. [specialisation: supported](https://doc.rust-lang.org/book/ch10-02-traits.html#using-trait-bounds-to-conditionally-implement-methods)
 4. You can pass a reference `&[mut] T` to the template parameter of a `struct`.
