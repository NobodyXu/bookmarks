 1. [Check number of arguments passed to a Bash script](https://stackoverflow.com/questions/18568706/check-number-of-arguments-passed-to-a-bash-script)
 2. Extract commandline arg in range `[n, m]`:
 
 ```bash
 echo ${@:n:m}
 ```
 
 If you want `[n, +Inf)`, then:
 
 ```bash
 echo ${@:n}
 ```
