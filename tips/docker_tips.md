 - Backup docker volume:
   
   ```bash
    #!/bin/bash
    
    if [ $# != 2 ]; then
        echo Usage "$0": volume /path/of/the/dir/in/volume/to/backup
        exit 1
    fi
    
    if [ -t 1 ]; then
        echo The output of the cmd is binary data "(tar)", \
             and it should be redirected instead of printed to terminal
        exit 1
    fi
    
    volume="$1"
    path="$2"
    
    exec docker run --rm --mount type=volume,src="$volume",dst=/mnt/volume/ alpine tar cf - . -C /mnt/volume/"$path"
   ```

   Adpated from [StackOverflow - How to port data-only volumes from one host to another?](https://stackoverflow.com/questions/21597463/how-to-port-data-only-volumes-from-one-host-to-another).
 - Backup docker volume incrementally using `rsync`:
   
   ```
   #!/bin/bash
   
   if [ $# != 3 ]; then
       echo Usage "$0": volume /path/of/the/dir/in/volume/to/backup /path/to/put/backup
       exit 1
   fi
   
   volume="$1"
   volume_path="$2"
   path="$3"
   
   if [[ "$path" =~ ^.*/$ ]]; then
       echo "The 3rd argument shouldn't end in '/', otherwise rsync would not behave as expected"
       exit 1
   fi
   
   container_name="docker-backup-rsync-service-$RANDOM"
   docker run --rm --name="$container_name" -d -p 8738:873 \
       --mount type=volume,src="$volume",dst=/mnt/volume/ \
       nobodyxu/rsyncd
   
   echo -e '\nStarting syncing...'
   
   rsync --info=progress2,stats,symsafe -aHAX --delete \
       "rsync://localhost:8738/root/mnt/volume/$volume_path/"  "$path"
   exit_status=$?
   
   echo -e '\nStopping the rsyncd docker...'
   docker stop -t 1 "$container_name"
   
   exit $exit_status
   ```
