 - `setarch `uname -m` -R <cmd> [<args>...]` for temporarily disable
 - Write `0` to `/proc/sys/kernel/randomize_va_space` to disable ASLR, 
         `1` to enable only conservative randomization.
   
   To disable ASLR permanently, create `/etc/sysctl.d/01-disable-aslr.conf` containing:
   
   ``` 
   kernel.randomize_va_space = 0
   ```
