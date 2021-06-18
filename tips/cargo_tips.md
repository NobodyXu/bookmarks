 - You can use `build.rustflags` defined in `${PROJECT}/.cargo/config` to 
   configure link flags used to link against your c code.
   
   E.x.

   ```
   [build]
   rustflags = ["-C", "link-args=-fuse-ld=lld -flto"]
   ```
 - How to debug test?
   
   ```
   cargo install cargo-with
   cargo with gdb -- test
   ```

 - How to disassemble test and dismangle symbol names?
   
   ```
   cargo with 'objdump -d' -- test | rustfilt
   ```
