 1. [Virtual Serial Port for Linux](https://stackoverflow.com/questions/52187/virtual-serial-port-for-linux)
    
    TL;DR:
    
    ```
    sudo socat PTY,user=$USER,link=/dev/ttyS10 STDIO
    ```
