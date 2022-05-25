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

 - Use `cargo supply-chain` to lists the crates depended on and people with publishing rights.
 - Use `cargo tree` to recursively list all deps of a crate.
 - Use `cargo geiger --all-features` to print statistics on use of `unsafe` in the crate and its dependencies.
 - Use `cargo audit` to check for vulnerabilities in the dependencies
 - Use `cargo crev` to review crates. [Getting started](https://github.com/crev-dev/cargo-crev/blob/master/cargo-crev/src/doc/getting_started.md)
 - Use [`cargo llvm-cov`](https://github.com/taiki-e/cargo-llvm-cov) for code coverage.
   
   It is much faster than cargo-tarpaulin
 - To upgrade all binary crates installed via `cargo install`,
   first install third-party crate by using `cargo install cargo-update`,
   then execute `cargo install-update -a` to upgrade all of the upgradable binary crates.
 - Use `RUSTFLAGS=-Zprint-type-sizes cargo +nightly build --release` to print sizes of types.
 - Use `cargo upgrade --skip-compatible` to upgrade dependencies that have new major releases,
   it is part of the binary crate `cargo-edit`.
 - Use `target=$(rustc -vV | grep host | cut -d : -f 2)` to detect the current target,
   which will output something like ` aarch64-apple-darwin`.
