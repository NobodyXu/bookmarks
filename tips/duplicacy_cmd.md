 - duplicacy init <snapshot id> <storage url>
 - duplicacy backup -t <tag> -stats -threads 2
   <br>If using sftp, make sure `-limit-rate 1100` is passed to the commands above.
   <br>Also, backup for hours might slow the speed down, so you can stop the backup by ctrl + c (it will be saved) and restart it after a couple of minutes.
   <br>This is due to the firewall deployed in server farms rate limit ssh connection and shut them down if they takes too much resources,
   <br>and if frequent TCP handshake is sent to the ssh port, it will classify them as DDOS and further rate-limit them.
 - save passwd: https://forum.duplicacy.com/t/passwords-credentials-and-environment-variables/1094
 - [Copy data between different storages efficiently, without the client as a bottlenect](https://forum.duplicacy.com/t/back-up-to-multiple-storages/1075)
   
   TL;DR:

   ```
   # log in to your local storage server
   mkdir -p \path\to\dummy\repository
   cd \path\to\dummy\repository
   duplicacy init repository_id onsite_storage_url
   duplicacy add -copy default offsite_storage --bit-identical repository_id offsite_storage_url
   duplicacy copy -from default -to offsite_storage
   ```

   By using `copy` on the server, the data flows from local_server -> router -> offsite_storage.

   if the offsite_storage are also on the local_server, i.e., migrate SFTP to minio, then data flows from 

   ```
   local_disk ->
   kernel ->
   duplicacy ->
   kernel (linux kernel would transfer 127.0.0.1 efficiently, without passing to network stack at all) ->
   minio ->
   kernel ->
   local_disk
   ```

   Since the data doesn't leave the machine, there is also no need to use TLS or any encryption.

   Edit:

   Even better if you use s3/minio/sftp/webdav or any other method that store your data as-is on the filesystem
   and it is run locally on your server:

   ```
   # log in to your local storage server
   mkdir -p \path\to\dummy\repository
   cd \path\to\dummy\repository
   duplicacy init repository_id onsite_storage_url
   duplicacy add -copy default /path/to/storage/data --bit-identical repository_id offsite_storage_url
   duplicacy copy -from default -to /path/to/storage/data
   ```

   if the offsite_storage are also on the local_server, i.e., migrate SFTP to minio, then data flows from 

   ```
   local_disk ->
   kernel ->
   duplicacy ->
   kernel ->
   local_disk
   ```
