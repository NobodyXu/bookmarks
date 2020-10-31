 1. The only generic known way to cancel a thread is to use `Thread.interrupt`.
    But `System.in.read` might not be interruptable.
 2. For `InputStream`, you can consider `InputStream.close()`, but it is not suggested.
