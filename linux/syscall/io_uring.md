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
