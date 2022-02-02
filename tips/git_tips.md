 - `git pull --rebase <upstream> main` would rebase the current branch with `<upstream>` master
 - `git bundle create path/to/bundle/to/create --all` for creating a bundle out of git repo
 - `git gc --aggressive --prune=now --keep-largest-pack` can be used to shrink repository size on disk if no other gc is running
 - `git rebase <commit/HEAD~number> -i` to collapse several commits into one or rewriting commit message.
 - `git rebase --exec 'git commit --amend --no-edit -n -s' -i HEAD` to fix unsigned old commits, learnt from [here](https://superuser.com/questions/397149/can-you-gpg-sign-old-commits)
 - To use a different git email in certain dir, check [this](https://stackoverflow.com/a/43654115/8375400).
 - `git rebase --onto BASE_BRANCH <COMMIT>` to rebase `<COMMIT>` onto `BASE_BRANCH`.
   
   Super useful when the main branch has squashed merge another PR, and your new PR
   is developed based on that squashed PR.
 - `git reset HEAD~1` revert the last unpushed commit.
