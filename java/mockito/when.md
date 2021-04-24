 1. [Mockito test a void method throws an exception](https://stackoverflow.com/questions/15156857/mockito-test-a-void-method-throws-an-exception/15157021)
 2. [Mocking Void Methods with Mockito](https://www.baeldung.com/mockito-void-methods)
    
    TL;DR:
    
    ```
    doAnswer(invocation -> {
        Object arg0 = invocation.getArgument(0);
        Object arg1 = invocation.getArgument(1);
        
        assertEquals(3, arg0);
        assertEquals("answer me", arg1);
        return null;
    }).when(myList).add(any(Integer.class), any(String.class));
    ```
    
    Can also replace `doAnswer` with `doThrow` according to 1.
