 1. [String Interning in Python: A Hidden Gem That Makes Your Code Faster](https://medium.com/techtofreedom/string-interning-in-python-a-hidden-gem-that-makes-your-code-faster-9be71c7a5f3e)
    
    TL;DR:
     - str interning can help speed up str comparison. If both `str` is interned, then comparing is equvalent to `x is y`
     - Use `sys.intern(str)` for explicit string interning
