 1. [Recoverable Errors with Result](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html)
 2. `unwrap()` automatically returns the embedded value, or panic
 3. `expect("...")` is similar to `unwrap()` except that you can customize panic message
 4. `unwrap_or(alternative__val)` either returns the embedded value, or return the `alternative_val`
 5. `unwrap_or_else(fn)` either returns the embedded value, or execute `fn` and return it
 6. `unwrap_or_default()` either returns the embedded value, or return the default value for the type `Defualt::default`
