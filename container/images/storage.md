 1. [Storage Drivers in Docker: A Deep Dive](https://integratedcode.us/2016/08/30/storage-drivers-in-docker-a-deep-dive/)
 
 > vfs is the “naive” implementation of the interface that does not use a union filesystem or CoW techniques at all, but rather 
 > copies all the layers in order into a static subdirectory and mounts the end result as the container root filesystem. It is 
 > not meant for real (production) use but is very valuable for simple validation and testing of other parts of the Docker 
 > engine. 
 
 Now I know why there is no build cache when using `vfs` driver.
 
 > Again, given ZFS is not a file-based implementation, the memory sharing capabilities of aufs and overlay are not available   
 > here in ZFS.
 
 Doubt that.
