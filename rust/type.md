 1. [primitive type - never](https://doc.rust-lang.org/nightly/std/primitive.never.html)
 2. [crate - fixed point float](https://docs.rs/fixed/1.9.0/fixed/)
    
    [crate - fixed_sqrt](https://docs.rs/fixed-sqrt/0.2.4/fixed_sqrt/)
    
    [crate - cordic](https://docs.rs/cordic/0.1.5/cordic/)
 3. [crate- bytemuck](https://docs.rs/bytemuck/1.6.1/bytemuck/index.html)
 4. [Exotically sized types](https://doc.rust-lang.org/nomicon/exotic-sizes.html)
 5. [Alternative representations](https://doc.rust-lang.org/nomicon/other-reprs.html)
 6. [`const fn size_of<T>() -> usize`](https://doc.rust-lang.org/std/mem/fn.size_of.html)
 7. [`const fn size_of_val<T>(val: &T) -> usize`](https://doc.rust-lang.org/std/mem/fn.size_of_val.html)

## method vs static function

```rust
struct S {
    i: i32
}

impl S {
    fn f1(a: i32) -> i32 {
        a
    }
    
    fn f2(b: &S) -> i32 {
        b.i
    }
    
    fn f3(&self) -> i32 {
        self.i
    }
    
    /*Error:
    fn f4(self: i32) -> i32 {
        self
    }*/
}

fn main() {
    let s = S { i: 1 };
    
    println!("S::f1(1) = {}", S::f1(1));
    println!("S::f2(s) = {}", S::f2(&s));
    // println!("s.f2() = {}", s.f2()); error!

    println!("s.f3() = {}", s.f3());
    println!("S::f3(&s) = {}", S::f3(&s));
}
```

## Destructor
 1. [`fn std::mem::forget<T>(t: t)`](https://doc.rust-lang.org/nightly/std/mem/fn.forget.html)
 2. [`#[repr(transparent)] struct ManuallyDrop<T: ?Sized>`](https://doc.rust-lang.org/nightly/std/mem/struct.ManuallyDrop.html)

## operater overloading
 1. [How do I make a struct callable?](https://stackoverflow.com/questions/42859330/how-do-i-make-a-struct-callable)
    
    TL;DR:
    
    Can't do it in stable Rust as of Jun, 2021, but it can be simulated with the `Deref` trait to return a lambda.


## Interior Mutability
 1. [Interior Mutability - The Rust Reference](https://doc.rust-lang.org/reference/interior-mutability.html)
    
    TL;DR:
    
    Use [`std::cell::UnsafeCell`](https://doc.rust-lang.org/std/cell/struct.UnsafeCell.html)
