## Time
 1. [chronotope/chrono](https://github.com/chronotope/chrono)

## parallel programming
 1. [rayon-rs/rayon](https://github.com/rayon-rs/rayon)

## Database
 1. [tokio-rs/rdbc](https://github.com/tokio-rs/rdbc)
 2. [diesel-rs/diesel](https://github.com/diesel-rs/diesel)

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

## GUI
 1. [Rust-Qt](https://github.com/rust-qt)
    <br>[Rust + Qt guide](https://rust-qt.github.io/qt/)

## Development
 1. [tokio-rs/loom](https://github.com/tokio-rs/loom)
    
    Testing concurrent bugs
    
 2. [bheisler/criterion.rs](https://github.com/bheisler/criterion.rs)
    
    For benchmarking
    
 

## Languagne binding for C++
 1. [rust-qt/Ritual](https://github.com/rust-qt/ritual)
