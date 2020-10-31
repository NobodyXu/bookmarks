 1. The only generic known way to cancel a thread is to use `Thread.interrupt`.
    
    But `System.in.read` might not be interruptable.
    <br>An alternative approach is to [create an intermediate stream](https://stackoverflow.com/questions/49520625/how-to-interrupt-reading-on-system-in)
    
    Another alternative is to make the thread that utilizes `System.in.read` as a proxy that copies everything into a buffer.
    <br>(Deprecated) [Creating a Synchronized Buffer for Producer/Consumer pattern in Java](https://stackoverflow.com/questions/17244889/creating-a-synchronized-buffer-for-producer-consumer-pattern-in-java)
    <br>[BlockingQueue](https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/BlockingQueue.html)
 2. For `InputStream`, you can consider `InputStream.close()`, but it is not suggested.
