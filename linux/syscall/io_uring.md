 1. [axboe/linuring](https://github.com/axboe/liburing)
 2. [Welcome to Lord of the io_uring](https://unixism.net/loti/)
    
    [Example programs from the Lord of the io_uring guide](https://github.com/shuveb/loti-examples)
 
 3. [axboe/liburing - feature requests: submit requests from any thread #109](https://github.com/axboe/liburing/issues/109)
    
    > But basically, you setup the first ring as usual. Then for subsequent rings where you want to share the async backend, you set io_uring_params->wq_fd to that first ring file descriptor, and ensure that you set IORING_SETUP_ATTACH_WQ in the setup flags as well.
    > That's it.
    > 
    > 
    > > That is, the interface that the user-space application sees is the same, though the backend is shared?
    > 
    > Correct, it behaves the exact same way.
 4. [axboe/liburing - Any possibility to add io_uring_prep_sendfile? #173](https://github.com/axboe/liburing/issues/173)
    
    > It basically consist of a pipe, and setting the size of that to something that works for your use case. Then you splice data to it from a file (for example, or vmsplice() data from your address space), and then you splice from it to a socket.
 5. [axboe/liburing - io_uring is slower than epoll #189](https://github.com/axboe/liburing/issues/189)
 6. automatic buffer selection:
    
           IORING_OP_PROVIDE_BUFFERS
              This command allows an application to register a group of buffers to be used by commands that read/receive data. Using buffers in this manner can eliminate the need  to  separate  the  poll  +
              read,  which  provides  a convenient point in time to allocate a buffer for a given request. It's often infeasible to have as many buffers available as pending reads or receive. With this fea‐
              ture, the application can have its pool of buffers ready in the kernel, and when the file or socket is ready to read/receive data, a buffer can be selected for the operation.  fd must  contain
              the number of buffers to provide, addr must contain the starting address to add buffers from, len must contain the length of each buffer to add from the range, buf_group must contain the group
              ID of this range of buffers, and off must contain the starting buffer ID of this range of buffers. With that set, the kernel adds buffers starting with the memory address in addr, each with  a
              length of len.  Hence the application should provide len * fd worth of memory in addr.  Buffers are grouped by the group ID, and each buffer within this group will be identical in size accord‐
              ing to the above arguments. This allows the application to provide different groups of buffers, and this is often used to have differently sized buffers available depending on what the  expec‐
              tations  are  of  the individual request. When submitting a request that should use a provided buffer, the IOSQE_BUFFER_SELECT flag must be set, and buf_group must be set to the desired buffer
              group ID where the buffer should be selected from. Available since 5.7.
          
           IOSQE_BUFFER_SELECT
              Used in conjunction with the IORING_OP_PROVIDE_BUFFERS command, which registers a pool of buffers to be used by commands that read or receive data. When buffers are  registered  for  this  use
              case,  and  this  flag  is  set  in  the  command,  io_uring will grab a buffer from this pool when the request is ready to receive or read data. If succesful, the resulting CQE will have IOR‐
              ING_CQE_F_BUFFER set in the flags part of the struct, and the upper IORING_CQE_BUFFER_SHIFT bits will contain the ID of the selected buffers. This allows the application to know exactly  which
              buffer  was  selected  for  the  operation.  If no buffers are available and this flag is set, then the request will fail with -ENOBUFS as the error code. Once a buffer has been used, it is no
              longer available in the kernel pool. The application must re-register the given buffer again when it is ready to recycle it (eg has completed using it). Available since 5.7.
   
   [io_uring support for automatic buffers](https://lwn.net/Articles/813311/)
