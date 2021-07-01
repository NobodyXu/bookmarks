 - [How do I print the full value of a long string in gdb?](https://stackoverflow.com/questions/233328/how-do-i-print-the-full-value-of-a-long-string-in-gdb)
   
   ```
   set print elements 0
   ```
 - Load core file: `gdb exe core`
 - Print variables of arbitary functions present on stack: https://stackoverflow.com/questions/6261392/printing-all-global-variables-local-variables
   
   ```
   (gdb) bt
   (gdb) select-frame <frame-no>
   (gdb) info locals
   ```
 - Print memory mappings of a core file:
    - `info proc mappings`
    - `info files`
    - `maintenance info sections`
 - How to print siginfo from a core file: `print $_siginfo` in gdb after the core file is loaded
   
   Learnt from [Finding Source of a UNIX Signal from Coredump](https://stackoverflow.com/questions/25519152/finding-source-of-a-unix-signal-from-coredump)
 - Use `x/d $rsp` to print memory pointed to by `$rsp`. Similarly, `$rsp` can be replaced
   with any value.
 - Print the source code of function using `list`
