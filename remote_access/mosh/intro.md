## Mosh

[mosh][1] is designed to be able to run on poor internet condition and provides robust and responsive connection.

It supports:
 - roaming to different IP without dropping connection
 - intermittent connectivity
 - intelligent local echo and line editing to reduce the effects of "network lag" on high-latency connections

Mosh uses `UDP` instead of `TCP` to
 - avoid blocking all subsequence packages when one is lost
 - transmit the latest screen and skipping the intermediate state
 
and it use State Synchronization Protocol to only **transmit** changed part of screen.

More onto the details [here][2].

[1]: https://mosh.org
[2]: https://mosh.org/#techinfo
