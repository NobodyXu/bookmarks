 1. [ramfs, rootfs and initramfs](https://www.kernel.org/doc/Documentation/filesystems/ramfs-rootfs-initramfs.txt)
 2. [Guide for decompressing initramfs](https://superuser.com/questions/734124/need-to-uncompress-the-initramfs-file)
    
    Note that your own initramfs can be compressed by `xz`, so don't just copy paste command.
    
    Use `file` to determine the compression method first, decompress it and then create a new dir and use `cpio -id < <decompressed>`
 3. initramfs (in cpio format) can be xz-compressed, and it might be even smaller than xz-compressed squashfs as it doesn't support random access.
 4. [Embedding initramfs into the kernel](https://wiki.gentoo.org/wiki/Custom_Initramfs#Embedding_into_the_Kernel)
    
    Note that initramfs must have `/dev/console`, eitherwise it won't be output anything at all.
 5. [Custom Initramfs](https://wiki.gentoo.org/wiki/Custom_Initramfs)
    
    Note that [Integrated initramfs does not always update](https://wiki.gentoo.org/wiki/Custom_Initramfs#Integrated_initramfs_does_not_always_update), and you can
    use the following snippet to force update:
    
    ```
    rm /usr/src/linux/usr/initramfs_data.cpio*
    ```
 6. [Do I need to update initramfs on every kernel recompilation?](https://unix.stackexchange.com/questions/632617/do-i-need-to-update-initramfs-on-every-kernel-recompilation)
 7. [Why `genkernel` decides to only include 4 modules in my `initramfs`?](https://unix.stackexchange.com/questions/632626/why-genkernel-decides-to-only-include-4-modules-in-my-initramfs)
 8. [Read only Initramfs Linux system](https://stackoverflow.com/questions/43891240/read-only-initramfs-linux-system)
    
    TL;DR:
    
    initramfs is created and mounted as an empty filesystem, then populate it with the content of cpio archive.
    
    To make it rdonly, use `mount -o remount,ro /`.
