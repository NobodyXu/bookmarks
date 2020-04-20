#ifndef  _GNU_SOURCE
# define _GNU_SOURCE
#endif

#ifndef  _POSIX_C_SOURCE
# define _POSIX_C_SOURCE 200809L
#endif

#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>

#include <iostream>
#include <stdio.h>
#include <err.h>

#define FMT(field) #field ": " << statbuf. field << std::endl

auto& operator << (std::ostream &out, const struct timespec &ts)
{
    return out << "sec: " << ts.tv_sec << " nsec: " << ts.tv_nsec;
}

int main() {
    struct stat statbuf;

    int fd = open("a", O_PATH);
    if (fd >= 0)
        printf("fd = %d\n", fd);
    else
        err(1, "open");

    int ret = fstatat(fd, "", &statbuf, AT_EMPTY_PATH);
    if (ret == -1)
        err(1, "fstatat");
    
    std::cout << FMT(st_dev)
              << FMT(st_ino)
              << FMT(st_mode)
              << FMT(st_nlink)
              << FMT(st_uid)
              << FMT(st_gid)
              << FMT(st_rdev)
              << FMT(st_size)
              << FMT(st_blksize)
              << FMT(st_blocks)
              << FMT(st_atim)
              << FMT(st_mtim)
              << FMT(st_ctim);

    return 0;
}
