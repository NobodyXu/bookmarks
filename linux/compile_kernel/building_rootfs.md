 1. [Change linux kernel installation directory](https://stackoverflow.com/questions/35931157/change-linux-kernel-installation-directory)
    
    TL;DR:
    
    ```
    INSTALL_PATH=/boot make install
    ```
    
 3. [Exporting kernel headers for use by userspace](https://www.kernel.org/doc/Documentation/kbuild/headers_install.txt)
    
    TL;DR:
    
    ```
    make headers_install INSTALL_HDR_PATH=/usr
    ```
