## container
 1. [kanidm/concread](https://github.com/kanidm/concread)
 2. [jonhoo/left-right]
    uses two hashmap, where one is read only (can serve multiple readers) and another is write only.
    <br>Optimize for reading (scale linearly, never blocked by writing) while makes writing slower.
 3. [jonhoo/evmap](https://github.com/jonhoo/evmap) built upon [jonhoo/left-right]
 4. [xacrimon/dashmap] uses `Box<[RwLock<HashMap<...>]>` underlying
 5. [withoutboats/waitmap](https://github.com/withoutboats/waitmap) built upon [xacrimon/dashmap]
 6. [jonhoo/flurry](https://github.com/jonhoo/flurry)

[xacrimon/dashmap]: https://github.com/xacrimon/dashmap
[jonhoo/left-right]: https://github.com/jonhoo/left-right
