 1. [Sane configuration for fast-forward][1]
    
    TL;DR
    
    ```
    git config --global pull.ff only   # Disallows non ff merges on pull
    git config --global merge.ff false # fast forward on merging from other branches is a crime
    
    # rebase instead of merge when pulling
    # since this is not merging from other branches, keeping a merge commit is useless
    git config --global pull.rebase true
    ```
 2. [Setup multiple git identities & git user informations](https://gist.github.com/bgauduch/06a8c4ec2fec8fef6354afe94358c89e)
    
    [Fork](https://gist.github.com/NobodyXu/be1fc773f7fdab6defd80ded8a9a68e8)
 
 
[1]: https://stackoverflow.com/a/48408368
