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
 2. [How do I iterate over a range with a custom step?](https://stackoverflow.com/questions/27893223/how-do-i-iterate-over-a-range-with-a-custom-step)
    
    TL;DR: `(1..10).step_by(<step>)`
