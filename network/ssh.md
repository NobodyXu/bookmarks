 1. [ssh vs openvpn tunneling](https://blog.backslasher.net/ssh-openvpn-tunneling.html)
 
 TL;DR
  
 ssh nails for single port forward and _**does not have [TCP over TCP][1] problem**_
  
 > @Nitz TCP tunnels in ssh do not use any TCP over TCP. In fact the ssh client is usually run with insufficient privileges to
 > even do it. And no, ssh does not strip any TCP headers from packets, because it never even touches a TCP packet. ssh is 
 > just an application making use of the TCP stack in the kernel, like any other application. Data travels through one TCP
 > connection from some program to the ssh client. The ssh client encrypts the data and send it through the TCP connection to
 > the server. The server decrypts it ans send it through the third TCP connection to a program at the other end. – kasperd

[1]: http://sites.inka.de/bigred/devel/tcp-tcp.html
