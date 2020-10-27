## pros

 1. [advantages of `emerge` vs binary package](https://www.reddit.com/r/Gentoo/comments/a5mdqz/advantages_of_emerge_vs_binary_package/)
    
    > case1:
    > 
    > let's say you want to patch a low level library/package that everything depends on, or use a development version of it. but the modification will break everything that depends on it and require a rebuild of a lot of things.
    > 
    > on gentoo, this is a non-issue because you build packages from source anyway so this will resolve itself during their installation. on binary distro, you would have to rebuild every single thing that depends on that package. and then all the updates of these packages and keep them updated.
    > 
    > case2:
    > 
    > let's say you have a package that builds with gcc7 but not gcc8, and there is no patch for gcc8 yet. gentoo allows you to keep multiple versions of compilers installed side-by-side, avoiding the problem by switching to older gcc.
    > 
    > case3:
    > 
    > you have a lot of packages that pull code directly from git repositories. gentoo's package manager can help you rebuild them when
    > 
    > they become incompatible due to system updates
    > 
    > there are new commits in their repositories
    > 
    > all of that in just one command. you can't do that with AUR, as far as i can tell.
    > 
    > case4:
    > 
    > you need a cross-compiler toolchain for architecture XYZ. you install crossdev on gentoo and it will create one for you, as long as gcc supports it.
    > 
    > case5:
    > 
    > you are interested in llvm development, and you'd like to build your entire OS with llvm/clang compiler. no problem on gentoo, as long as things build and work.
    > 
    > case6:
    > 
    > you want to hold certain package at specific version. as long as it doesn't break builds of other packages depending on it, your system will work just fine. examples may include a database server, specific version of php for writing your scripts, specific version of java runtime, etc. or you might want to use older glibc, for some reason.
    > 
    > that also applies to the kernel.
    > 
    > case7:
    > 
    > you need multiple versions of some software installed side-by-side, like a database server, java runtime or something else. gentoo lets you do that, in most cases.
    > 
    > tl;dr - if you tinker a lot with your system or use it for development/server purposes, gentoo is for you.

