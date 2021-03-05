 1. How to setup:
    
    First, enable network access (otherwise you server will not be able to access internet):
    
    ```
    iptables -A INPUT -j ACCEPT
    iptables -A OUTPUT -j ACCEPT
    iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    iptables -A OUTPUT -m conntrack --ctstate NEW,ESTABLISHED,RELATED -j ACCEPT
    ```
    
    Then enable your ssh port:
    
    ```
    sudo iptables -A INPUT -p tcp --dport <your_ssh_port> -j ACCEPT
    ```
   
    You should also enable other ports you need by replacing `<your_ssh_port>` with each of these ports.
    
    Then blacklist all other ports:
    
    ```
    sudo iptables -P INPUT DROP
    ```
    
    After verifing that you **can access `ssh` and other services**, install and enable [iptables-persistent]:
    
    ```
    sudo apt-get install iptables-persistent
    ```
    
    During installation, it will prompt you on whether to save current `iptables` configuration, select 'yes'.
    
    Now restart your server and `ssh` into it.
    
    Use `sudo iptables -L` to verify that your rules are indeed saved.
    
    Reference:
     - [How to configure iptables on Ubuntu](https://upcloud.com/community/tutorials/configure-iptables-ubuntu/)
       
       This guide here made a **serious mistake**: it will block your access to internet from server, i.e. `ping` and `curl` all fail.
       
       Check the guide below to understand how to fix this.
       
     - [No client internet access when setting up these iptables rules](https://askubuntu.com/questions/79525/no-client-internet-access-when-setting-up-these-iptables-rules)
    
 2. [iptables persistent]
 
[iptables persistent]: https://unix.stackexchange.com/a/52522
