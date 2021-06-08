 1. [Why does Rust not have a return value in the main function, and how to return a value anyway?](https://stackoverflow.com/questions/24245276/why-does-rust-not-have-a-return-value-in-the-main-function-and-how-to-return-a)
    
    TL;DR:
    
    ```
    fn main() -> Result<(), Error type here> {
       Ok(())
    }
    ```
