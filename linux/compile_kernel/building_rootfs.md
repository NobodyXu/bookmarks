 1. [Change linux kernel installation directory](https://stackoverflow.com/questions/35931157/change-linux-kernel-installation-directory)
    
    TL;DR:
    
    ```
    INSTALL_PATH=/boot make install
    ```
 2. [Enabling IP forwarding at kernel compile time](https://unix.stackexchange.com/questions/123981/enabling-ip-forwarding-at-kernel-compile-time)
    
 3. [Exporting kernel headers for use by userspace](https://www.kernel.org/doc/Documentation/kbuild/headers_install.txt)
    
    TL;DR:
    
    ```
    make headers_install INSTALL_HDR_PATH=/usr
    ```
