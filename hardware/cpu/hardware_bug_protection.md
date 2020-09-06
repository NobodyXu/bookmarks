 1. [Address Space Isolation (ASI): Speculative execution protection - Google](https://linuxplumbersconf.org/event/7/contributions/708/attachments/497/1132/Address_Space_Isolation_-_LPC_-_RC001.pdf)
    
    Technoglogies that offers speculative execution protection and tries to be performant:
     - Intel - unmap guest memory from the direct map (KVM protected memory)
        - One VM cannot access memory of another VM
     - IBM - protecting containers
        - Allocate namespace-private memory
        - Per-process private (userspace) memory
        - Remove mapping from the global page-table
     - Oracle
        - KVM address space isolation, similar to google's effort (e.g. #pf-fork)
     - Amazon
        - Allocate process local memory, removed from the direct map.
     - Google
        - Address Space Isolation - protects sensitive data
        - Separate page table for domains of different privilege
