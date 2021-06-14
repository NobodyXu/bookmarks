 1. [`fn catch_unwind<F: FnOnce() -> R + UnwindSafe, R>(f: F) -> Result<R>`](https://doc.rust-lang.org/std/panic/fn.catch_unwind.html)
 2. [`Trait std::panic::UnwindSafe`](https://doc.rust-lang.org/std/panic/trait.UnwindSafe.html)
 3. [`fn set_hook(hook: Box<dyn Fn(&PanicInfo<'_>) + Sync + Send + 'static>)`](https://doc.rust-lang.org/std/panic/fn.set_hook.html)
 4. [`fn take_hook() -> Box<dyn Fn(&PanicInfo<'_>) + Sync + Send + 'static>`](https://doc.rust-lang.org/std/panic/fn.take_hook.html)
