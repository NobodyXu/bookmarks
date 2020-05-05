 1. [Unix domain socket - Wikipedia][1]
 2. [Does UNIX Domain Sockets Overflow?][2]
 
 TL;DR
 
 No, and it is always reliable, given that it is a `stream`, `datagram` or `sequenced-packet`.
 
 3. [Difference between UNIX domain STREAM and DATAGRAM sockets?][3]
 4. [Can I share a file descriptor to another process on linux or are they local to the process?][4]
 5. [TCP loopback connection vs Unix Domain Socket performance][5]
 
 6. Easiest way to create a pair of connected unix socket:
 
 ```
 int sv[2];
 socketpair(AF_UNIX, SOCK_DGRAM, 0, sv);
 ```
 
 7. [What's the practical limit on the size of single packet transmitted over domain socket?][6]

[1]: https://en.wikipedia.org/wiki/Unix_domain_socket
[2]: https://unix.stackexchange.com/questions/283323/do-unix-domain-sockets-overflow
[3]: https://stackoverflow.com/questions/13953912/difference-between-unix-domain-stream-and-datagram-sockets
[4]: https://stackoverflow.com/questions/2358684/can-i-share-a-file-descriptor-to-another-process-on-linux-or-are-they-local-to-t
[5]: https://stackoverflow.com/questions/14973942/tcp-loopback-connection-vs-unix-domain-socket-performance
[6]: https://stackoverflow.com/questions/21856517/whats-the-practical-limit-on-the-size-of-single-packet-transmitted-over-domain
