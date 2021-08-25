 - flag `--info` provides for fine-grind progress output control
 - `-aHAX --delete /path/to/src/dir/ /path/to/dest/dir` fully sync all contents under src to dest.
   <br>Notice that the dest path doesn't have the trailing '/' and it is intentional.
 - Use `--inplace` option (implies `--partial`) to ensure that the upload is resumable and will not create
   copies on the remote filesystem on resume.
