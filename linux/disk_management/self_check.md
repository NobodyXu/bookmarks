## It is suggested to run self check and repair after power supply cut off

_**WARNING: ALWAYS UNMOUNT FILESYSTEM BEFORE DOING SELF CHECK AND REPAIRING!**_

 - `sudo fsck -V /dev/ext4_paritition`
 - `sudo xfs_repair -v /dev/xfs/paritition`
