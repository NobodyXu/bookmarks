 1. [Ptys (Pseudo terminals) internal buffer size](https://superuser.com/questions/1195103/ptys-pseudo-terminals-internal-buffer-size)
 
    TL;DR
    
    [`ptsbufsize.py`](https://superuser.com/a/1452858/855807):
    
    ```python3
    #!/usr/bin/env python3
    import os
    from pty import openpty
    from fcntl import fcntl, F_GETFL, F_SETFL
    from itertools import count
    
    def set_nonblock(fd):
        flags = fcntl(fd, F_GETFL)
        flags |= os.O_NONBLOCK
        fcntl(fd, F_SETFL, flags)
    
    master, slave = openpty()
    
    set_nonblock(slave)
    
    for i in count():
        try:
            os.write(slave, b'a')
        except BlockingIOError:
            i -= 1
            break
    
    print("pts write blocked after {} bytes ({} KiB)".format(i, i//1024))
    ```
 
 2. [What are the responsibilities of each Pseudo-Terminal (PTY) component (software, master side, slave side)?](https://unix.stackexchange.com/questions/117981/what-are-the-responsibilities-of-each-pseudo-terminal-pty-component-software)
 3. [Session-Management on Linux](https://dvdhrm.wordpress.com/2013/08/24/session-management-on-linux/)
 4. [How VT-switching works](https://dvdhrm.wordpress.com/2013/08/24/how-vt-switching-works/)
 5. [Why use `-T` with ssh](https://stackoverflow.com/q/42505339/8375400)
