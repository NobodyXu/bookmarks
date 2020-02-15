# What is time command, an executable or just a shell builtin?

Read this [answer][1] which says that:

> Users of the bash shell need to use an explicit path in order to run
> the external time command and not the shell builtin variant.  On system
> where time is installed in /usr/bin, the first example would become
>       /usr/bin/time wc /etc/hosts

Verified on my computer:

```
$ type time
time is a shell keyword

$ help time
time: time [-p] pipeline
    Report time consumed by pipeline's execution.
    
    Execute PIPELINE and print a summary of the real time, user CPU time,
    and system CPU time spent executing PIPELINE when it terminates.
    
    Options:
      -p        print the timing summary in the portable Posix format
    
    The value of the TIMEFORMAT variable is used as the output format.
    
    Exit Status:
    The return status is the return status of PIPELINE.
```

The [answer][1] answers this [question][2]

# A deeper dive into `time` and `/usr/bin/time`:

[/usr/bin/time: not the command you think you know][3]

[1]: https://askubuntu.com/a/434294/772092
[2]: https://askubuntu.com/questions/434289/why-doesnt-the-time-command-work-with-any-option
[3]: https://hackernoon.com/usr-bin-time-not-the-command-you-think-you-know-34ac03e55cc3
