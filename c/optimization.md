 1. [How are x86 uops scheduled, exactly?][3]
 2. [Is performance reduced when executing loops whose uop count is not a multiple of processor width?][1]
 3. [Can x86's MOV really be “free”? Why can't I reproduce this at all?][2]
 4. [Intel® 64 and IA-32 Architectures Software Developer Optimization Manuals][4]
 
## Compiler flags

 1. `-fno-unwind-tables -fno-asynchronous-unwind-tables` for remving majority of `.eh_frame`.
     This might break:
      - `backtrace()`
      - `__attribute__((__cleanup__(f)))`
      - `__builtin_return_address(n)`, for $n > 0$
      - `pthread_cleanup_push`, implemented in terms of `__attribute__((__cleanup__(f)))`
 2. [C compiler merge code option]
 3. Pass `--icf=all` to linker merge any identical functions.
    Pass `--icf=safe` to linker only merge identical functions whose address are not taken.
 4. Pass `--gc-sections` to linker to remove unused sections.
 5. To use `-flto` with `-Oz`, you need to also pass `-Wl,--plugin-opt=O3`.
 6. Use of `-flto` can shrink size of generated binary.

## AutoFDO
 1. [Intro to AutoFDO](https://linuxplumbersconf.org/event/7/contributions/798/attachments/661/1214/LTO_PGO_and_AutoFDO_-_Plumbers_2020_-_Tolvanen_Wendling_Desaulniers.pdf)
 2. [google AutoFDO source](https://github.com/google/autofdo)

## BOLT
 1. [BOLT](https://github.com/facebookincubator/BOLT)

[1]: https://stackoverflow.com/questions/39311872/is-performance-reduced-when-executing-loops-whose-uop-count-is-not-a-multiple-of
[2]: https://stackoverflow.com/questions/44169342/can-x86s-mov-really-be-free-why-cant-i-reproduce-this-at-all/44193770#44193770
[3]: https://stackoverflow.com/questions/40681331/how-are-x86-uops-scheduled-exactly
[4]: https://software.intel.com/content/www/us/en/develop/articles/intel-sdm.html#optimization
[C compiler merge code option]: https://stackoverflow.com/questions/25194738/do-c-compilers-de-duplicate-merge-code
