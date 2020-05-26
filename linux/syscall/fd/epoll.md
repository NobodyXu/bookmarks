 1. [If a file is readable before epoll_ctl is called in edge-triggered mode, will a subsequent epoll_wait return immediately?][1]
 2. [what's the best way to remove fd from epoll in my case?][2]
 3. [EPOLLIN and EPOLLRDHUP][3]
 4. [How do I use EPOLLHUP][4]
 5. [How does epoll's EPOLLEXCLUSIVE mode interact with level-triggering?][5]
 6. [TCP: When is EPOLLHUP generated?][6]
 
## Design Flaw

 1. [Epoll is fundamentally broken 1/2 for multithreaded app][7]
 
[1]: https://stackoverflow.com/questions/12920243/if-a-file-is-readable-before-epoll-ctl-is-called-in-edge-triggered-mode-will-a
[2]: https://stackoverflow.com/questions/21255784/whats-the-best-way-to-remove-fd-from-epoll-in-my-case
[3]: https://stackoverflow.com/questions/16473393/given-any-epoll-tcp-socket-event-if-epollrdhup-0-and-epollin-1-is-a-subsequent
[4]: https://stackoverflow.com/questions/6437879/how-do-i-use-epollhup/6438173
[5]: https://stackoverflow.com/questions/41582560/how-does-epolls-epollexclusive-mode-interact-with-level-triggering
[6]: https://stackoverflow.com/questions/52976152/tcp-when-is-epollhup-generated
[7]: https://idea.popcount.org/2017-02-20-epoll-is-fundamentally-broken-12/
