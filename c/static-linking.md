 1. [library order in static linking](https://eli.thegreenplace.net/2013/07/09/library-order-in-static-linking)
 2. [C symbol visibility in static archives](https://stackoverflow.com/questions/39981491/c-symbol-visibility-in-static-archives)
    
    > `#define PUBLIC __attribute__ ((visibility("default")))` then mark `myfn()` as `PUBLIC` in `myfn.c`. Don't mark anything else `PUBLIC`.
    > 
    > Compile objects with `gcc -c foo.c bar.c baz.c myfn.c -fvisibility=hidden`, which marks everything as hidden except for `myfn()`.
    > 
    > Create a convenience archive using `ld`'s partial-linking switch: `ld -r foo.o bar.o baz.o myfn.o -o libmyfn.a`
    > 
    > Localise everything that wasn't PUBLIC like so: `objcopy --localize-hidden libmyfn.a`
    > 
    > Now `nm` says `myfn` is the only global symbol in `libmyfn.a` and subsequent linking into other programs works just fine: `gcc -o main main.c -L. -lmyfn`
    > (here, the program calls `myfn()`; if it tried to call `foo()` then compilation would fail).
    
    After investigation of `man objcopy` and `man llvm-objcopy`, I also found the following options of interest:
     - `--localize-symbol=symbolname`:
       Convert a global or weak symbol called symbolname into a local symbol, so that it is not visible externally.
       This option may be given more than once.
       Note - unique symbols are not converted.
     - `--localize-symbols=filename`:
       Apply --localize-symbol option to each symbol listed in the file filename.
       Filename is simply a flat file, with one symbol name per line.
       Line comments may be introduced by the hash character.
       This option may be given more than once.
     - `-x` or `--discard-all`:
       Do not copy non-global symbols from the source file.
     - `--strip-unneeded`:
       Strip all symbols that are not needed for relocation processing.
     - `--strip-unneeded-symbol=symbolname`:
       Do not copy symbol symbolname from the source file unless it is needed by a relocation.  This option may be given more than once.
     - `--strip-unneeded-symbol=symbolname`:
       Do not copy symbol symbolname from the source file unless it is needed by a relocation.  This option may be given more than once.
 3. [How to merge two “ar” static libraries into one?](https://stackoverflow.com/questions/3821916/how-to-merge-two-ar-static-libraries-into-one)
    
    ```
    libtool --mode=link cc -static -o libaz.la libabc.la libxyz.la
    ```
