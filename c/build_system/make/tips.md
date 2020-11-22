## prebuild

Adapted from [Force Makefile to execute script before building targets](https://stackoverflow.com/questions/2122602/force-makefile-to-execute-script-before-building-targets/41604044):

```makefile
prebuild_result = $(shell ...)
```
