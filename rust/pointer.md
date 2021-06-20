 1. [`to_raw_parts(self)` method of primitive type pointer](https://doc.rust-lang.org/nightly/std/primitive.pointer.html#method.to_raw_parts)
    
    ```rust
    #![feature(ptr_metadata)]
    
    trait Trait {
        fn f(&self) -> i32;
    }
    
    struct Struct {
        i: i32
    }
    
    impl Trait for Struct {
        fn f(&self) -> i32 {
            self.i
        }
    }
    
    fn main() {
        let s = Struct { i: 1 };
        let sp = &s as *const _;
        
        let (sdynp, sdynvtable) = (&s as &dyn Trait as *const dyn Trait).to_raw_parts();
        
        println!("sp = {:p}", sp);
        
        println!("sdynp = {:p}, sdynvtable = {:#?}", sdynp, sdynvtable);
    }
    ```
    
 2. [`struct std::ptr::DynMetadata`](https://doc.rust-lang.org/nightly/std/ptr/struct.DynMetadata.html)
 3. [`trait core::ptr::Pointee`](https://doc.rust-lang.org/nightly/core/ptr/trait.Pointee.html)
