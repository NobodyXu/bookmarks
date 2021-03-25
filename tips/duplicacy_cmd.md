 - duplicacy init <snapshot id> <storage url>
 - duplicacy backup -t <tag> -stats -threads 2
   <br>If using sftp, add `-limit-rate 1100` to the commands above and make sure `-threads 2` is supplied.
   <br>Also, backup for hours might slow the speed down, so you can stop the backup by ctrl + c (it will be saved) and restart it after a couple of minutes.
 - save passwd: https://forum.duplicacy.com/t/passwords-credentials-and-environment-variables/1094
