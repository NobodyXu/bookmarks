 1. [3 Facts of the Integer Caching in Python](https://medium.com/techtofreedom/3-facts-of-the-integer-caching-in-python-20ce587f09bb)
    
    TL;DR:
     - Different implementations and versions of Python may have different mechanisms for the same feature.
     - The integers in the range of [-5, 256] are singletons in CPython and can’t be recreated again.
     - If the CPython compiler can see the whole code, more optimisations may apply to the code (create only one integer object, thus can be compared using `is` instead of `==`)
