 - If after ssh, `tmux` failed due to `unsuitable $TERM (alacrity or etc)`, set `export TERM=screen-256color`
 - If `ssh` suddenly asks you accept new server identity when you have already accepted 
   one before, uses `ssh-keyscan -p <port> <host>` to see if previous identity and new identity 
   are both present.
