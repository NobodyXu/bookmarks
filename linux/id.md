 1. [Is the uid_t type signed or unsigned?](https://stackoverflow.com/questions/21370094/is-the-uid-t-type-signed-or-unsigned)

## gid
The urls below contains explanataions to the concept of `supplementary group`.

 1. [Group Identifier](https://en.wikipedia.org/wiki/Group_identifier)
 2. [Manage Linux Group in Linux](https://www.techrepublic.com/article/tech-tip-manage-user-groups-in-linux/)

[Always setgroups before setuid?](https://security.stackexchange.com/questions/122141/always-setgroups-before-setuid)

Yes, otherwise `setgroups` will fail.

 > if you setuid to a non-zero value first (meaning you're no longer root), then call setgroups, the effective uid of the  ?
 > process is now no longer root, meaning that the internal setgid call fails.
