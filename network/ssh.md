 1. [ssh vs openvpn tunneling](https://blog.backslasher.net/ssh-openvpn-tunneling.html)
 
 TL;DR
  
 ssh nails for single port forward and _**does not have [TCP over TCP][1] problem**_
  
 > @Nitz TCP tunnels in ssh do not use any TCP over TCP. In fact the ssh client is usually run with insufficient privileges to
 > even do it. And no, ssh does not strip any TCP headers from packets, because it never even touches a TCP packet. ssh is 
 > just an application making use of the TCP stack in the kernel, like any other application. Data travels through one TCP
 > connection from some program to the ssh client. The ssh client encrypts the data and send it through the TCP connection to
 > the server. The server decrypts it ans send it through the third TCP connection to a program at the other end. – kasperd

 2. [ssh multiplexing](https://en.m.wikibooks.org/wiki/OpenSSH/Cookbook/Multiplexing)
 3. [scanssh - wikibooks](https://en.m.wikibooks.org/wiki/OpenSSH/Third_Party_Utilities#scanssh)
 4. [sshfp](https://en.m.wikibooks.org/wiki/OpenSSH/Third_Party_Utilities#sshfp)
 
 Publish ssh fingerprint to DNS record, so that the identity of the ssh server can be confirmed.
 
 5. [ssh-audit](https://github.com/arthepsy/ssh-audit)
 
 It can list ssh server information.
 
 6. [Mitigating SSH based attacks – Top 15 Best SSH Security Practices](https://securitytrails.com/blog/mitigating-ssh-based-attacks-top-15-best-security-practices)
 
[1]: http://sites.inka.de/bigred/devel/tcp-tcp.html
