 1. [How To Reuse SSH Connection To Speed Up Remote Login Process Using Multiplexing]
 2. [OpenSSH cookbook - Multiplexing]
 
    TL;DR:
    
    > Port Forwarding using multiplexing
    > 
    > It is possible to request port forwarding without having to establish new connections. Here we forward port 8080 on the local host to port 80 on the remote host using -L:
    > 
    > ```
    > $ ssh -O forward -L 8080:localhost:80 -S ~/.ssh/controlmasters/fred@server.example.org:22  server.example.org
    > ```
    > 
    > The same can be done for remote forwarding, using -R. The escape sequence ~C is not available for multiplexed sessions, so -O forward is the only way to add port forwarding on the fly.
 
[How To Reuse SSH Connection To Speed Up Remote Login Process Using Multiplexing]: https://www.cyberciti.biz/faq/linux-unix-reuse-openssh-connection/
[OpenSSH cookbook - Multiplexing]: https://en.m.wikibooks.org/wiki/OpenSSH/Cookbook/Multiplexing
