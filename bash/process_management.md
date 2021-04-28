 1. [Wait for a process to finish](https://stackoverflow.com/questions/1058047/wait-for-a-process-to-finish)
    
    TL;DR:
    
    ```
    tail --pid=$pid -f /dev/null
    ```
    
    If you are on alpine, then you need to `apk add coreutils`.
