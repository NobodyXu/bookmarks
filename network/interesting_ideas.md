 1. [Hacker News- Discussion on "Why do we use the Linux kernels TCP stack?"](https://news.ycombinator.com/item?id=12021195)
 
 Take away:
  - Do not write your own implementation unless:
    - You have enough people around to support
    - The other ends's behavior is well under your control
  - But currently there are userspace implementations that is better than the in-kernel ones, like
    - [DPDK](https://www.dpdk.org)
    - [Netmap](http://info.iet.unipi.it/~luigi/netmap/)
    
 2. [LWN: Improving Linux networking performance](https://lwn.net/Articles/629155/)
