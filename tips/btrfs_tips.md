# mounting
 - suggested to use `noatime,discard=async,nofail,compress=zstd:15`.
   
   `nofail` is there just in case btrfs is corrupted.

   `noatime,discard=async` are there to optimise btrfs.

   `compress=zstd:15` is used to compress compressible with zstd, level 15 (currently the highest).

# Create snapshot

```
btrfs subvolume snapshot -r /subvolume_or_root /subvolume_or_root/path/to/snapshot
sync
```

`path/to/snapshot` is usually something like `.snapshot/<snapshot_name>`, where the snapshot will be mounted
as a subvolume.

# Incremental Backup by hand

Shamelessly copied from [official doc](https://btrfs.wiki.kernel.org/index.php/Incremental_Backup)

## Initial bootstrap

```
btrfs send /path/to/snapshot | ... | btrfs receive /path/to/snapshot/dir
```

`/path/to/snapshot` should be kept around for the next backup, so that the data can be sent
incrementally.

## Reductive

We can now send the difference between the old and new backup to the backup volume:

```
btrfs send /path/to/snapshot /path/to/new/snapshot | ... | btrfs receive /path/to/snapshot/dir
```

Now we can delete the old snapshot on local machine:

```
btrfs subvolume delete /path/to/snapshot
mv /path/to/new/snapshot /path/to/snapshot
```

You can do the same on the remote if you want.
