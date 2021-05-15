 1. [What is the difference between Swing and AWT?](https://stackoverflow.com/questions/408820/what-is-the-difference-between-swing-and-awt)

## Threading
 1. [The Event Dispatch Thread](https://docs.oracle.com/javase/tutorial/uiswing/concurrency/dispatch.html)
 2. [Init threads](https://docs.oracle.com/javase/tutorial/uiswing/concurrency/initial.html)
    
    TL;DR:
    
    You must call this in your main thread:
    
    ```
    SwingUtilities.invokeLater(new Runnable() {
        public void run() {
            createAndShowGUI();
        }
    });
    ```
 3. [Swing's Threading Policy](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/javax/swing/package-summary.html#threading)
 4. [AWT Threading Issues](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/doc-files/AWTThreadIssues.html#ListenersThreads)
