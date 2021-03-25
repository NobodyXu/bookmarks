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
