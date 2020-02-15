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
```

The [answer] answers this [question][2]

[1]: https://askubuntu.com/a/434294/772092
[2]: https://askubuntu.com/questions/434289/why-doesnt-the-time-command-work-with-any-option
