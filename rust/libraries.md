[libc](https://crates.io/crates/libc)

## Helpers
 1. [init_array](https://crates.io/crates/init_array)
 2. [Lucretiel/iterate](https://docs.rs/iterate/1.0.0/iterate/macro.iterate.html)
 3. [once_cell](https://docs.rs/once_cell/1.8.0/once_cell/index.html) for (lazy/delayed) initializing global data and lazy evaluate local variable
 4. [fergaljoconnor/zero_v](https://github.com/fergaljoconnor/zero_v) A framework for iterating over collections of types implementing a trait without virtual dispatch
 5. [matthieu-m/static-rc](https://github.com/matthieu-m/static-rc) Compile-time reference counting
 6. [dtolnay/no-panic](https://github.com/dtolnay/no-panic) Attribute macro to require that the compiler prove a function can't ever panic
 7. [illicitonion/num_enum](https://github.com/illicitonion/num_enum) help convert enum to/from integer
 8. [jaemk/cached](https://github.com/jaemk/cached)
 9. [edgeandnode/eventuals](https://github.com/edgeandnode/eventuals) observer pattern
 10. [calebzulawski/multiversion](https://github.com/calebzulawski/multiversion) for dynamic and static dispatch of the same function optimized for different CPU model
 11. [anixe/doku](https://github.com/anixe/doku) Doku is a framework for building documentation with code-as-data methodology in mind.
 12. [systemcluster/staticfilemap](https://github.com/systemcluster/staticfilemap) Procedural macro to embed optionally compressed files during compilation.
 13. [CAD97/pointer-utils/crates/slice-dst](https://github.com/CAD97/pointer-utils/tree/master/crates/slice-dst) 
     
     > Support for custom slice-based DSTs.
     > 
     > By handling allocation manually, we can manually allocate the Box for a custom DST. So long as the size lines up with what it should be, once the metadata is created, Rust actually already handles the DSTs it already supports perfectly well, safely! Setting them up is the hard part, which this crate handles for you.
 
 14. [CAD97/pointer-utils](https://github.com/CAD97/pointer-utils)
     
     > Pointer utility crates
     > 
     > erasable: Erase pointers of their concrete type.
     > rc-borrow: Borrowed forms of Rc and Arc.
     > rc-box: Known unique forms of Rc and Arc.
     > ptr-union: Pointer unions the size of a pointer.
     > slice-dst: Support for custom slice-based DSTs.


## cmdline parsing
 1. [TeXitoi/structopt](https://github.com/TeXitoi/structopt)

## signal handling
 1. [vorner/signal-hook](https://github.com/vorner/signal-hook) it will be great to support signal handling as async fn

## err handling
 1. [dtolnay/anyhow](https://github.com/dtolnay/anyhow)
 2. [dtolnay/thiserror](https://github.com/dtolnay/thiserror) for designing your own `Error` type

## Integer Parsing
 1. [gilescope/atoi_radix10](https://github.com/gilescope/atoi_radix10)
## Time
 1. [chronotope/chrono](https://github.com/chronotope/chrono)

## Generator
 1. [tokio-rs/async-stream](https://github.com/tokio-rs/async-stream)

## parallel programming
 1. [rayon-rs/rayon](https://github.com/rayon-rs/rayon)

## simd
 1. [AdamNiederer/faster](https://github.com/AdamNiederer/faster)

## Database
 1. [tokio-rs/rdbc](https://github.com/tokio-rs/rdbc)
 2. [diesel-rs/diesel](https://github.com/diesel-rs/diesel)
 3. [launchbadge/SQLx](https://github.com/launchbadge/sqlx)

## async io framework
 1. [tokio-rs/tokio]
 2. [tokio-rs/mio]
    
    Mio is a fast, low-level I/O library for Rust focusing on non-blocking APIs and event notification for building high performance I/O apps with as little overhead as possible over the OS abstractions.
    
    [io-uring support](https://github.com/tokio-rs/mio/issues/923)
    <br>Might land in 2.0 series
    
    Used by [tokio-rs/tokio]
 3. [tokio-rs/io-uring](https://github.com/tokio-rs/io-uring)
    
    Used by [tokio-rs/mio]
    
 4. [spacejam/rio](https://github.com/spacejam/rio)

[tokio-rs/tokio]: https://github.com/tokio-rs/tokio
[tokio-rs/mio]: https://github.com/tokio-rs/mio

## networking
 1. [tower-rs/tower](https://github.com/tower-rs/tower)
    
    Tower is a library of modular and reusable components for building robust networking clients and servers.
    
### HTTP

#### low-level
 1. [hyperium/hyper](https://github.com/hyperium/hyper)
    
    hyper can be both client and server
 
    [RUST IN CURL WITH HYPER](https://daniel.haxx.se/blog/2020/10/09/rust-in-curl-with-hyper/)
    
    Basically, hyper is rewriting the internals of curl while keeping its API as of right now (2021).
 2. [cloudflare/quiche](https://github.com/cloudflare/quiche)
#### high-level

##### client
 1. [seanmonstar/reqwest](https://github.com/seanmonstar/reqwest)

##### web-server
 1. [seanmonstar/warp](https://github.com/seanmonstar/warp)
 2. [http-rs/tide](https://github.com/http-rs/tide)
 3. [SergioBenitez/Rocket](https://github.com/SergioBenitez/Rocket)
 4. [actix.rs](https://actix.rs)

## TUI

 1. [gyscos/cursive](https://github.com/gyscos/cursive)
 2. [ihalila/pancurses](https://github.com/ihalila/pancurses) supports both unix and win
 3. [dankamongmen/notcurses-rs](https://github.com/dankamongmen/notcurses-rs) binding for notcurses

## GUI
 1. [Rust-Qt](https://github.com/rust-qt)
    <br>[Rust + Qt guide](https://rust-qt.github.io/qt/)
 2. [linebender/druid](https://github.com/linebender/druid)
 3. [emilk/egui](https://github.com/emilk/egui) seems quite easy to use and support wasm and opengl out of box

## Development
 1. [tokio-rs/loom](https://github.com/tokio-rs/loom)
    
    Testing concurrent bugs
    
 2. [bheisler/criterion.rs](https://github.com/bheisler/criterion.rs)
    
    For benchmarking
    
 3. [asomers/mockall](https://github.com/asomers/mockall) powerful mock object library for rust
 4. [xd009642/tarpaulin](https://github.com/xd009642/tarpaulin) for test coverage

## Data Sci
 1. [pola-rs/polars](https://github.com/pola-rs/polars) pandas in rust

## ML
 1. [tensorflow/rust](https://github.com/tensorflow/rust) tensorflow binding for rust
 2. [LaurentMazare/tch-rs](https://github.com/LaurentMazare/tch-rs) pytorch binding for rust

## Crypto
 1. [dalek-cryptography](https://github.com/dalek-cryptography)
 2. [Rust Crypto](https://github.com/RustCrypto)

## BPF
 1. [foniod/redbpf](https://github.com/foniod/redbpf)

## FFI
 1. [dtolnay/cxx](https://github.com/dtolnay/cxx)
