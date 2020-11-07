 1. [How can I undo the last commit?](https://www.git-tower.com/learn/git/faq/undo-last-commit/)
 2. [How to rename commits with wrong author in git](https://stackoverflow.com/questions/38133775/how-to-rename-commits-with-wrong-author-in-git)
    
    TL;DR
    
    ```bash
    git commit --amend --author="John Doe <someone@example.com>"
    ```
    
    For multiple commits:
    
    
    ```bash
    git filter-branch --commit-filter '
        if [ "$GIT_COMMITTER_NAME" = "<Old Name>" ];
        then
                GIT_COMMITTER_NAME="<New Name>";
                GIT_AUTHOR_NAME="<New Name>";
                GIT_COMMITTER_EMAIL="<New Email>";
                GIT_AUTHOR_EMAIL="<New Email>";
                git commit-tree "$@";
        else
                git commit-tree "$@";
        fi' HEAD `
    ```
