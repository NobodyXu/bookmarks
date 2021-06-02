 1. How to calculate `max`?
    
    ```rust
    pub fn max<T: PartialOrd>(list: &[T]) -> Option<&T> {
        list.iter().reduce(
            |a, b| {
                if a > b {
                    &a
                } else {
                    &b
                }
            }
        )
    }
    ```
    
    or
    
    ```rust
    pub fn max<T: PartialOrd>(list: &[T]) -> Option<&T> {
        if list.is_empty() {
            return Option::None
        }
    
        let mut largest = &list[0];
        for each in &list[1..] {
            if each > largest {
                largest = &each
            }
        }
    
        Option::Some(largest)
    }
    ```
