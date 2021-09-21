 1. [async programming in rust](https://rust-lang.github.io/async-book/01_getting_started/04_async_await_primer.html)
 2. [why async fn in traits are hard](https://smallcultfollowing.com/babysteps/blog/2019/10/26/async-fn-in-traits-are-hard/)
 3. [dtolnay/async-trait](https://github.com/dtolnay/async-trait)
 4. [Async/Await - The challenges besides syntax - Cancellation](https://gist.github.com/Matthias247/ffc0f189742abf6aa41a226fe07398a8)
 5. Calling `async` functions in `Drop::drop` implementation:
    
    ```
    use tokio::runtime::{Builder, Handle};

    if /* [optional] Already closed */ {
        return;
    }

    let f = || async move {
        // The actualy async drop code here
    };

    if let Ok(handle) = Handle::try_current() {
        // If blocking is necessary, calls `futures::executor::block_on` on
        // the `JoinHandle` returned by `handle.spawn(f())`.
        //
        // However, if the current tokio runtime is `current_thread`, then the method
        // described above just won't work.
        //
        // You would have to use `spin_on::spin_on` instead to archive the same effect,
        // but more inefficient.
        //
        // So, TLDR, don't use blocking unless necessary.
        handle.spawn(f());
    } else {
        let rt = Builder::new_current_thread() // The new Runtime will use current_thread
            .enable_all() // Enable IO and timer driver if available
            .build() // Build and return Result<Runtime>
            .unwrap();

        rt.block_on(f());
    }
    ```
