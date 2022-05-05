 1. [model-checking/kani](https://github.com/model-checking/kani) Kani Rust Verifier
    
    Kani is particularly useful for verifying unsafe code in Rust, where many of the language's usual guarantees are no longer checked by the compiler. Kani verifies:
    
     - Memory safety (e.g., null pointer dereferences)
     - User-specified assertions (i.e., assert!(...))
     - The absence of panics (e.g., unwrap() on None values)
     - The absence of some types of unexpected behavior (e.g., arithmetic overflows)
