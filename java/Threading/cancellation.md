 1. The only generic known way to cancel a thread is to use `Thread.interrupt`.
    
    But `System.in.read` might not be interruptable.
    <br>An alternative approach is to [create an intermediate stream](https://stackoverflow.com/questions/49520625/how-to-interrupt-reading-on-system-in).
    <br>Another alternative is to make the thread that utilizes `System.in.read` as a proxy that copies everything into a buffer.
 2. For `InputStream`, you can consider `InputStream.close()`, but it is not suggested.
