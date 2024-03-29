[libc](https://crates.io/crates/libc)

## Configuration
 1. [cuviper/autocfg](https://github.com/cuviper/autocfg)
    A Rust library for build scripts to automatically configure code based on compiler support. Code snippets are dynamically tested to see if
    the rustc will accept them, rather than hard-coding specific version support.
 2. [alexcrichton/cfg-if](https://github.com/alexcrichton/cfg-if)
    A macro to ergonomically define an item depending on a large number of #[cfg] parameters. Structured like an if-else chain,
    the first matching branch is the item that gets emitted.

## Memory allocator
 1. [sebastiencs/shared-arena](https://github.com/sebastiencs/shared-arena)
    
    Memory pools are usefull when allocating and deallocating lots of data of the same size.
    Using a memory pool speed up those allocations/deallocations.

## Iterator
 1. [jDomantas/internal-iterator](https://github.com/jDomantas/internal-iterator) Internal iterator equivalent of `std::iter::Iterator`.

## In-Process (self) Sandbox
 1. [oustrophedon/extrasafe](https://github.com/boustrophedon/extrasafe)

## Helpers
 1. [init_array](https://crates.io/crates/init_array)
 2. [Lucretiel/iterate](https://docs.rs/iterate/1.0.0/iterate/macro.iterate.html)
 3. [once_cell](https://docs.rs/once_cell/1.8.0/once_cell/index.html) for (lazy/delayed) initializing global data and lazy evaluate local variable
 4. [fergaljoconnor/zero_v](https://github.com/fergaljoconnor/zero_v) A framework for iterating over collections of types implementing a trait without virtual dispatch
 5. [matthieu-m/static-rc](https://github.com/matthieu-m/static-rc) Compile-time reference counting
 6. [dtolnay/no-panic](https://github.com/dtolnay/no-panic) Attribute macro to require that the compiler prove a function can't ever panic
 7. [illicitonion/num_enum](https://github.com/illicitonion/num_enum) help convert enum to/from integer
 8. [nolanderc/dyn_struct](https://github.com/nolanderc/dyn_struct) for creating objects from unsized struct
 9. [eolu/const-gen](https://github.com/eolu/const-gen) Generate complex data structure at compile time using build.rs
 10. [sunfishcode/io-lifetimes](https://github.com/sunfishcode/io-lifetimes) Provides implementation of `OwnedFd`, `BorrowedFd` and etc as described in [RFC3128](https://github.com/rust-lang/rfcs/blob/master/text/3128-io-safety.md)
 11. [okannen/static_init](https://gitlab.com/okannen/static_init)
 12. [maciejhirsz/beef](https://github.com/maciejhirsz/beef): Faster, more compact implementation of `std::borrow::Cow`
 13. [jan-auer/dynfmt](https://github.com/jan-auer/dynfmt) formatting strings dynamically, implement subset of `std::fmt`.
 14. [grayjack/sugars](https://github.com/grayjack/sugars) Syntax sugars for creating map, set, dequeue easily and comprehensive view (similar to comprehensive in python).
 15. [sagebind/castaway](https://github.com/sagebind/castaway) Experimental crate for zero-cost downcasting for limited compile-time specialization
 16. [Emoun/duplicate](https://github.com/Emoun/duplicate)  Easy code duplicate with substitution for Rust
 17. [lyonsyonii/akin](https://github.com/lyonsyonii/akin)  Rust crate for writing repetitive code easier and faster.
 18. [djkoloski/munge](https://github.com/djkoloski/munge) munge makes it easy and safe to destructure raw pointers, MaybeUninits, Cells, and Pins by prodoving destructing.
 19. [Peternator7/strum](https://github.com/Peternator7/strum) A small rust library for adding custom derives to enums
 20. [kas-gui/impl-tools](https://github.com/kas-gui/impl-tools) Helper macros: autoimpl, impl_scope

## Synchronoisation
 1. [Amanieu/parking_lot](https://github.com/Amanieu/parking_lot) Provides synchronisation primitives that are significantly faster and occupy less space compared to standard library implementation using posix

## Thread Local variables
 1. [amanieu/thread_local-rs](https://github.com/amanieu/thread_local-rs)
    
    > This library provides the ThreadLocal type which allow a separate copy of an object to be used for each thread.
    > This allows for per-object thread-local storage, unlike the standard library's thread_local! macro which only allows static thread-local storage.
    > 
    > Per-thread objects are not destroyed when a thread exits. Instead, objects are only destroyed when the ThreadLocal containing them is destroyed.
    > 
    > Note that since thread IDs are recycled when a thread exits, it is possible for one thread to retrieve the object of another thread.
    > Since this can only occur after a thread has exited this does not lead to any race conditions.

## Data structure
 1. [jaemk/cached](https://github.com/jaemk/cached)
 2. [edgeandnode/eventuals](https://github.com/edgeandnode/eventuals) observer pattern
 3. [calebzulawski/multiversion](https://github.com/calebzulawski/multiversion) for dynamic and static dispatch of the same function optimized for different CPU model
 4. [anixe/doku](https://github.com/anixe/doku) Doku is a framework for building documentation with code-as-data methodology in mind.
 5. [systemcluster/staticfilemap](https://github.com/systemcluster/staticfilemap) Procedural macro to embed optionally compressed files during compilation.
 6. [CAD97/pointer-utils/crates/slice-dst](https://github.com/CAD97/pointer-utils/tree/master/crates/slice-dst) 
     
     > Support for custom slice-based DSTs.
     > 
     > By handling allocation manually, we can manually allocate the Box for a custom DST. So long as the size lines up with what it should be, once the metadata is created, Rust actually already handles the DSTs it already supports perfectly well, safely! Setting them up is the hard part, which this crate handles for you.
 
 7. [CAD97/pointer-utils](https://github.com/CAD97/pointer-utils)
     
     > Pointer utility crates
     > 
     > - erasable: Erase pointers of their concrete type.
     > - rc-borrow: Borrowed forms of Rc and Arc.
     > - rc-box: Known unique forms of Rc and Arc.
     > - ptr-union: Pointer unions the size of a pointer.
     > - slice-dst: Support for custom slice-based DSTs.

 8. [Manishearth/triomphe](https://github.com/Manishearth/triomphe)
     
     > Fork of Arc. This has the following advantages over std::sync::Arc:
     > 
     > - triomphe::Arc doesn't support weak references: we save space by excluding the weak reference count, and we don't do extra read-modify-update operations to handle the possibility of weak references.
     > - triomphe::UniqueArc allows one to construct a temporarily-mutable Arc which can be converted to a regular triomphe::Arc later
     > - triomphe::OffsetArc can be used transparently from C++ code and is compatible with (and can be converted to/from) triomphe::Arc
     > - triomphe::ArcBorrow is functionally similar to &triomphe::Arc<T>, however in memory it's simply &T. This makes it more flexible for FFI; the source of the borrow need not be an Arc pinned on the stack (and can instead be a pointer from C++, or an OffsetArc). Additionally, this helps avoid pointer-chasing.
     > - triomphe::Arc has can be constructed for dynamically-sized types via from_header_and_iter
     > - triomphe::ThinArc provides thin-pointer Arcs to dynamically sized types
     > - triomphe::ArcUnion is union of two triomphe:Arcs which fits inside one word of memory
     > 
     > This crate is a version of servo_arc meant for general community use.
 9. [Lucretiel/brownstone](https://github.com/Lucretiel/brownstone) A library for constructing statically sized arrays
 10. [colin-kiegel/rust-derive-builder](https://github.com/colin-kiegel/rust-derive-builder) automatically creates builder for struct
 11. [idanarye/rust-typed-builder](https://github.com/idanarye/rust-typed-builder) automatically creates compile-time checked builder
 12. [kobzol/rust-delegate](https://github.com/kobzol/rust-delegate) delegate macro for Rust
 13. [japaric/heapless](https://github.com/japaric/heapless)
 14. [LPGhatguy/thunderdome](https://github.com/LPGhatguy/thunderdome)
     
     > Thunderdome is a generational arena inspired by generational-arena, slotmap, and slab. 
     > It provides constant time insertion, lookup, and removal via small (8 byte) keys (which can be converted to 4-byte slot) returned from Arena.
 15. [Gankra/thin-vec](https://github.com/Gankra/thin-vec)
     
     > `ThinVec` is a Vec that stores its length and capacity inline, making it take up less space.
     > Currently this crate mostly exists to facilitate gecko ffi.
     > The crate isn't quite ready for use elsewhere, as it currently unconditionally uses the libc allocator.
 16. [servo/rust-smallvec](https://github.com/servo/rust-smallvec)
 17. [andylokandy/smallbox](https://github.com/andylokandy/smallbox)
     
     > `SmallBox` optimization: store small item on stack and fallback to heap for large item. Requires Rust 1.36+.

## String
 1. [ParkMyCar/compact_str](https://github.com/ParkMyCar/compact_str) Has the same size as `String`; Can store at most 24 ascii character on stack.
 2. [rust-analyzer/smol_str](https://github.com/rust-analyzer/smol_str) Has the same size as `String`; Can store at most 22 bytes on stack.
 3. [Nugine/const-str](https://github.com/Nugine/const-str) Compile-time string operations.
 4. [vitiral/strfmt](https://github.com/vitiral/strfmt) formatting dynamic strings.
 5. [Kixiron/lasso](https://github.com/Kixiron/lasso) A fast, concurrent string interner.
 6. [zbraniecki/tinystr](https://github.com/zbraniecki/tinystr), provides:
     
     - TinyStr4 an ASCII-only string limited to 4 characters.
     - TinyStr8 an ASCII-only string limited to 8 characters.
     - TinyStr16 an ASCII-only string limited to 16 characters.
     - TinyStrAuto (enum):
        - Tiny when the string is 16 characters or less.
        - Heap when the string is 17 or more characters.

## Embed data into executable
 1. [rust-embed](https://crates.io/crates/rust-embed) Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev

## Integer
 1. [fastdiv](https://crates.io/crates/fastdiv) This crate performs fast division by a runtime constant divisor, by precomputing a division factor that can then be used repeatedly. We provide fast division for both u32 and u64.
 
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
 2. [ibraheemdev/seize](https://github.com/ibraheemdev/seize)

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
 2. [aya-rs/aya](https://github.com/aya-rs/aya)

## FFI
 1. [dtolnay/cxx](https://github.com/dtolnay/cxx)

## (De)serialisation

 1. [Diggsey/ijson](https://github.com/Diggsey/ijson)
