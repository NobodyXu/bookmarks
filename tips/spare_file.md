 - `fallocate --dig-holes <filename>` can convert any file to sparse file in place.
 - Allocate data blocks in files with holes:

   ```c
   static void fallocate_with_hole(int fd, size_t len) {
       if (lseek(fd, len - 1, SEEK_CUR) < 0) {
           err(1, "lseek failed");
       }
       if (write(fd, "1", 1) < 0) {
           err(1, "write failed");
       }
   }
   ```

 - Punch hole in files:

   ```
   static void punch_hole(int fd, off_t offset, off_t len) {
       if (fallocate(fd, FALLOC_FL_PUNCH_HOLE | FALLOC_FL_KEEP_SIZE, offset, len) < 0) {
           err(1, "fallocate failed to punch hole");
       }
   }
   ```
