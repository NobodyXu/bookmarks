## inheritance

 1. [Inheritance with Traits](https://riptutorial.com/rust/example/22917/inheritance-with-traits)
    
    TL;DR:
    
    ```
    impl<T> <traits> for T where T: <derived traits> {
        fn <fn>(&self, ...) -> ... {...}
        ...
    }
    ```