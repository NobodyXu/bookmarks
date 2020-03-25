 1. [Sane configuration for fast-forward][1]
 
 TL;DR
 
 ```
 git config --global pull.ff only   # Disallows non ff merges on pull
 git config --global merge.ff false # fast forward on merging from other branches is a crime
 
 # rebase instead of merge when pulling
 # since this is not merging from other branches, keeping a merge commit is useless
 git config --global pull.rebase true
 ```
 
[1]: https://stackoverflow.com/a/48408368
