## Testing
 1. [tokio-rs/loom](https://github.com/tokio-rs/loom) Concurrency permutation testing tool for Rust.

## container
 1. [kanidm/concread](https://github.com/kanidm/concread)
 2. [jonhoo/left-right]
    uses two hashmap, where one is read only (can serve multiple readers) and another is write only.
    <br>Optimize for reading (scale linearly, never blocked by writing) while makes writing slower.
 3. [jonhoo/evmap](https://github.com/jonhoo/evmap) built upon [jonhoo/left-right]
 4. [xacrimon/dashmap] uses `Box<[RwLock<HashMap<...>]>` underlying
 5. [withoutboats/waitmap](https://github.com/withoutboats/waitmap) built upon [xacrimon/dashmap]
 6. [jonhoo/flurry](https://github.com/jonhoo/flurry)
 7. [bzim/lockfree](https://gitlab.com/bzim/lockfree)
    
    Supports:
     - Per-Object Thread-Local Storage
     - Map, implemented using multi-level hash-tables (in a tree fashion) with ordered buckets
     - Set
     - Queue
     - Stack
     - SPSC, MPSC, SPMC and MPMC channels, fully asynchronous
 8. [vorner/arc-swap](https://github.com/vorner/arc-swap) Making Arc itself atomic
 9. [redox-os/chashmap](https://gitlab.redox-os.org/redox-os/chashmap)
    
    > This crate implements concurrent hash maps, based on bucket-level multi-reader locks. It has excellent performance characteristics¹ and supports resizing, in-place mutation and more.

[xacrimon/dashmap]: https://github.com/xacrimon/dashmap
[jonhoo/left-right]: https://github.com/jonhoo/left-right
