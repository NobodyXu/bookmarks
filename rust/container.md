 1. [Learn Rust With Entirely Too Many Linked Lists](https://rust-unofficial.github.io/too-many-lists/)
 2. How to implement `IntoIterator` for container that takes a reference instead of moving:
    
    ```rust
    impl<'a, T> IntoIterator for &'a List<T> {
        type Item = &'a T;                    
        type IntoIter = ListIterator<'a, T>;  
    
    fn into_iter(self) -> Self::IntoIter {
            self.iter()                       
        }                                     
    }
    ```

## Existing implementation
 1. [Fairglow/index-list](https://crates.io/crates/index_list)

### Concurrency Support

Check [concurrency::container](/rust/concurrency.md#container)
