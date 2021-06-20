 1. [non type parameters in generics](https://www.google.com/amp/s/amp.reddit.com/r/rust/comments/jy95xq/what_are_const_generics/)
    
    Supported

 2. Varadic generic: Not supported directly, but can be emulated using macro (print! for example is implemented using macro)
 3. [specialisation: supported](https://doc.rust-lang.org/book/ch10-02-traits.html#using-trait-bounds-to-conditionally-implement-methods)
 4. You can pass a reference `&[mut] T` to the template parameter of a `struct`.
 5. [Generic returns in Rust](https://blog.jcoglan.com/2019/04/22/generic-returns-in-rust/)
 6. [`trait std::marker::Unsize`](https://doc.rust-lang.org/std/marker/trait.Unsize.html)
    
    ```rust
    #![feature(ptr_metadata)]
    #![feature(unsize)]
    
    use std::marker::Unsize;
    
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
    
    struct Wrapper<'a, Trait: ?Sized> {
        reference: &'a Trait
    }
    
    impl<'a, Trait: ?Sized> Wrapper<'a, Trait> {
        fn new<T: Unsize<Trait>>(obj: &'a T) -> Wrapper<'a, Trait> {
            Wrapper{ reference: obj as &Trait}
        }
    }
    
    fn main() {
        let s = Struct { i: 1 };
        let sp = &s as *const _;
        
        let wrapper: Wrapper<dyn Trait> = Wrapper::new(&s);
        
        let (sdynp, sdynvtable) = (&s as &dyn Trait as *const dyn Trait).to_raw_parts();
        
        println!("sp = {:p}", sp);
        
        println!("sdynp = {:p}, sdynvtable = {:#?}", sdynp, sdynvtable);
        
        let (sdynp, sdynvtable) = (wrapper.reference as *const dyn Trait).to_raw_parts();
        println!("sdynp = {:p}, sdynvtable = {:#?}", sdynp, sdynvtable);
    }
    ```
    [playground link](https://play.rust-lang.org/?version=nightly&mode=debug&edition=2018&gist=e29cd4a845ff864bbe45babbff8db47b)
