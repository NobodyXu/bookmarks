 1. How to disable echo and canon mode in `termios`:
    
    ```java
    // local modes - echoing off, disable canon mode
    currOpts.c_lflag &= ~(ECHO | ICANON);
    // control chars - set return condition: min number of bytes and timer.
    // Return each byte, or zero for timeout.
    currOpts.c_cc[VMIN] = 1;
    // 100 ms timeout (unit is tens of second). Do not set this to 0 for
    // whatever reason, because this will skyrocket the cpu usage to 100%!
    currOpts.c_cc[VTIME] = 1;
    ```
 2. [Move the cursor in a C program](https://stackoverflow.com/questions/33025599/move-the-cursor-in-a-c-program)
