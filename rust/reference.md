 1. Please use `let [mut] <var_name> = &[mut]...;` to declare a reference where the first `mut` denotes whether the reference itself is mutable.
    <br>Don't use `let &mut <var_name> = ...`, which is a pattern matching and can create a value instead of a reference.
 2. [RustyYato/rel-ptr](https://github.com/RustyYato/rel-ptr)
 
