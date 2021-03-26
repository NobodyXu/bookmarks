 - duplicacy init <snapshot id> <storage url>
 - duplicacy backup -t <tag> -stats -threads 2
   <br>If using sftp, make sure `-limit-rate 1100` is passed to the commands above.
   <br>Also, backup for hours might slow the speed down, so you can stop the backup by ctrl + c (it will be saved) and restart it after a couple of minutes.
   <br>This is due to the firewall deployed in server farms rate limit ssh connection and shut them down if they takes too much resources,
   <br>and if frequent TCP handshake is sent to the ssh port, it will classify them as DDOS and further rate-limit them.
 - save passwd: https://forum.duplicacy.com/t/passwords-credentials-and-environment-variables/1094
