 1. [How does javac automatically compile dependencies of a class](https://stackoverflow.com/questions/30527632/how-does-javac-automatically-compile-dependencies-of-a-class)
 2. [Cannot find symbol in same package and directory](https://stackoverflow.com/questions/32598120/cannot-find-symbol-in-same-package-and-directory)
    
    TL;DR:
    
    If you want `javac main.java` to works while depending on other files under the same dir, then you need to:
    
    ```
    mkdir package.name
    mv <all other file.java> package.name/
    ```
    
    Then remove the `package` declaration in `main.java` and `import` other dependencies into it.
