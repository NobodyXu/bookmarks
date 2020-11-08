 1. [Backup and restore sqlite from disk to memory in Java](https://stackoverflow.com/questions/17548026/backup-and-restore-sqlite-from-disk-to-memory-in-java)
    
    TL;DR:
    
    ```java
    stat.executeUpdate("restore from '" + dbFile.getAbsolutePath() + "'");
    ```
    
    NOTE that `restore from` must be in lower case for it to work.
