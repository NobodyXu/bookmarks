 1. [How can I undo the last commit?](https://www.git-tower.com/learn/git/faq/undo-last-commit/)
 2. [How to rename commits with wrong author in git](https://stackoverflow.com/questions/38133775/how-to-rename-commits-with-wrong-author-in-git)
    
    TL;DR
    
    ```bash
    git commit --amend --author="John Doe <someone@example.com>"
    ```
    
    For multiple commits:
    
    
    ```bash
    git filter-branch --commit-filter '
        if [ "$GIT_COMMITTER_NAME" = "$OldName" ];
        then
                GIT_COMMITTER_NAME="$NewName";
                GIT_AUTHOR_NAME="$NewName";
                GIT_COMMITTER_EMAIL="$NewEmail";
                GIT_AUTHOR_EMAIL="$NewEmail";
                git commit-tree "$@";
        else
                git commit-tree "$@";
        fi' HEAD
    ```
 3. [Squash my last X commits together using Git](https://stackoverflow.com/questions/5189560/squash-my-last-x-commits-together-using-git)
    
    TL;DR:
    
    `git rebase -i HEAD~{COMMITS TO BE SQUASHED}` or `git rebase -i {after this commit}` then replace `pickup` on the line corresponds to the commits to be 
    squashed with `squash`.
 4. [Can you GPG sign old commits?](https://superuser.com/questions/397149/can-you-gpg-sign-old-commits)
    
    TL;DR:
    
    ```
    git rebase --exec 'git commit --no-edit --amend -s -S<keyid>' -i <branch/commit>
    ```
