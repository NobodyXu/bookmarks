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
