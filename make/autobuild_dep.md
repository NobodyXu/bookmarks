 1. [Auto-Dependency Generation][1]
 
    Example code:
 
    ```
    SRCS=$(shell find */* -type f -name '*.c')
    DEPS=$(SRCS:.c=.d)
    OBJS=$(SRCS:.c=.o)
    
    DEPFLAGS = -MT $@ -MMD -MP -MF $*.Td
    DEPFILES := $(SRCS:%.c=%.d)
    
    $(DEPFILES):
    include $(wildcard $(DEPFILES))
    
    # Disable implict pattern
    %.o : %.c
    %.o : %.c %.d
    $(CC) -c -o $@ $< $(CFLAGS) $(DEPFLAGS)
    mv -f $*.Td $*.d && touch $@
    ```
 
[1]: http://make.mad-scientist.net/papers/advanced-auto-dependency-generation/#include
