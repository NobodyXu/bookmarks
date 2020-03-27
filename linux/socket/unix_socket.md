 1. [Unix domain socket - Wikipedia][1]
 2. [Does UNIX Domain Sockets Overflow?][2]
 
 TL;DR
 
 No, and it is always reliable, given that it is a `stream`, `datagram` or `sequenced-packet`.
 
 3. [Difference between UNIX domain STREAM and DATAGRAM sockets?][3]
 4. [Can I share a file descriptor to another process on linux or are they local to the process?][4]
 
[1]: https://en.wikipedia.org/wiki/Unix_domain_socket
[2]: https://unix.stackexchange.com/questions/283323/do-unix-domain-sockets-overflow
[3]: https://stackoverflow.com/questions/13953912/difference-between-unix-domain-stream-and-datagram-sockets
[4]: https://stackoverflow.com/questions/2358684/can-i-share-a-file-descriptor-to-another-process-on-linux-or-are-they-local-to-t
