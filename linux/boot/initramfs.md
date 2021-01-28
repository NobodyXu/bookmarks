 1. [ramfs, rootfs and initramfs](https://www.kernel.org/doc/Documentation/filesystems/ramfs-rootfs-initramfs.txt)
 2. [Guide for decompressing initramfs](https://superuser.com/questions/734124/need-to-uncompress-the-initramfs-file)
    
    Note that your own initramfs can be compressed by `xz`, so don't just copy paste command.
 3. initramfs (in cpio format) can be xz-compressed, and it might be even smaller than xz-compressed squashfs as it doesn't support random access.
 4. [Embedding initramfs into the kernel](https://wiki.gentoo.org/wiki/Custom_Initramfs#Embedding_into_the_Kernel)
    
    Note that initramfs must have `/dev/console`, eitherwise it won't be output anything at all.
 5. [Custom Initramfs](https://wiki.gentoo.org/wiki/Custom_Initramfs)
