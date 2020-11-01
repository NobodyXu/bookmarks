 1. [Revert file after commit(s)](https://stackoverflow.com/a/953573/8375400)
    
    TL;DR:
    
    Recover file deleted `n` commit ago:
    
    ```
    git checkout $commit~n path/to/file.ext
    ```
    
    Recover file deleted in `$commit`:
    
    ```
    git checkout $commit path/to/file.ext
    ```
