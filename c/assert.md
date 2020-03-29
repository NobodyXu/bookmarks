 1. [assert() with message][1]
 
 TL;DR
 
 ```c
 #include <assert.h>
 
 int always_true(const char *msg) {
     return 1;
 }
 
 #define assert_msg(expr, msg) assert((expr) && always_true(msg))
 ```

[1]: https://stackoverflow.com/a/60910010/8375400
