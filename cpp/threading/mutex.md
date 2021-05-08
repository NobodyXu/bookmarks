 1. [Why is sizeof(std::mutex)==40 (gcc,clang,icc)? [duplicate]](https://stackoverflow.com/questions/16693992/why-is-sizeofstdmutex-40-gcc-clang-icc)
    
    TL;DR:
    
     - Prevent false sharing
     - underlying posix_mutex has many features and the lock can be acquired according to process priority
 2. [4 bytes Futex impl](https://ideone.com/F3Zozc)
 3. [boost::thread data structure sizes on the ridiculous side?](https://stackoverflow.com/questions/6816448/boostthread-data-structure-sizes-on-the-ridiculous-side)
