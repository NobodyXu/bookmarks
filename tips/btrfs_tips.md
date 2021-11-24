# `mkfs.btrfs`

It is suggested to use `-m dup` when creating the filesystem to have DUP metadata
even on a single disk to improve reliability.

If the filesystem has already `mkfs`ed, then use
`btrfs balance start -mconvert=dup /mount/point`.

It is also strongly recommended to enable `space_cache=v2` at `mkfs` time by passing
`-R free-space-tree` to `mkfs.btrfs`.

# mounting
 - suggested to use `noatime,discard=async,nofail,compress=zstd:15,flushoncommit`.
   
   `nofail` is there just in case btrfs is corrupted.

   `noatime,discard=async` are there to optimise btrfs.

   `compress-force=zstd:15` is used to compress compressible with zstd,
   level 15 (currently the highest).

   `compress-force` is used since btrfs already odes a check internally
   that is more efficient than the one btrfs does if `compress` is used.

   `flushoncommit` should be enabled to provide the same data on power-loss guarantee
   as ext4.

# Scrubbing (checking for errors)

To check a mounted btrfs:

```
btrfs scrub start -Bd <mountpoint>
```

`-B` means do not background
`-d` means stats per device

# Create snapshot

```
btrfs subvolume snapshot -r /subvolume_or_root /subvolume_or_root/path/to/snapshot
sync
```

`path/to/snapshot` is usually something like `.snapshot/<snapshot_name>`, where the snapshot will be mounted
as a subvolume.

# Incremental Backup by hand

Shamelessly copied from [official doc](https://btrfs.wiki.kernel.org/index.php/Incremental_Backup)

## How to send backup over network

Since network is usually very unstable and slow, and `btrfs send` as of writing outputs
uncompressed data (compressed data is supported in v2), it is suggested to first
compress it and store it locally:

```
sudo btrfs send /path/to/snapshot | zstd --progress --ultra --long -22 --rsyncable -T0 --exclude-compressed -o <file>.zst
```

Then transmit it using `rsync` to the remote computer in a resumable manner.

## Initial bootstrap

```
sudo btrfs send /path/to/snapshot | ... | btrfs receive /path/to/snapshot/dir
```

`/path/to/snapshot` should be kept around for the next backup, so that the data can be sent
incrementally.

## Reductive

We can now send the difference between the old and new backup to the backup volume:

```
sudo btrfs send -p /path/to/snapshot /path/to/new/snapshot | ... | btrfs receive /path/to/snapshot/dir
```

Now we can delete the old snapshot on local machine:

```
btrfs subvolume delete /path/to/snapshot
mv /path/to/new/snapshot /path/to/snapshot
```

You can do the same on the remote if you want.

# Swapfile on Btrfs

```
# Must be created in a subvolume, eitherwise snapshot won't work.
cd /path/to/btrfs
btrfs subvolume create swap
cd swap

truncate -s 0 swapfile

# Disable copy-on-write
chattr +C swapfile
# Disable compression
btrfs property set swapfile compression none

fallocate -l 512M swapfile
chmod 600 swapfile
mkswap swapfile
```
