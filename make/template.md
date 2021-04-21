 1. `Makefile` that supports automatic dependency building and supports configurable `BUILD_DIR` , 
    `TARGET_DIR` and configurable features.

    ```
    # Path
    BUILD_DIR ?= .
    TARGET_DIR := /usr/local
    
    # Features
    DEBUG ?= false
    
    # compiler and flags
    CC := clang
    CXX := clang++
    
    ifeq ($(DEBUG), false)
    	CFLAGS := -Wall -march=native -mtune=native -Oz -Wall -flto
    	CFLAGS += -fno-asynchronous-unwind-tables -fno-unwind-tables
    
    	CXXFLAGS := -fno-exceptions -fno-rtti
    
    	LDFLAGS := -s -flto -fuse-ld=lld -Wl,-icf=all,--gc-sections,--plugin-opt=O3,-O3,--as-needed
    else
    	CFLAGS := -Og -g -Wall
    endif
    
    CFLAGS += $(shell pkg-config --cflags libssh)
    LIBS := $(shell pkg-config --libs libssh)
    
    ## Objects to build
    C_SRCS := $(wildcard *.c)
    C_OBJS := $(C_SRCS:.c=.o)
    
    CXX_SRCS := $(wildcard *.cc)
    CXX_OBJS := $(CXX_SRCS:.cc=.o)
    
    OBJS := $(addprefix $(BUILD_DIR)/, $(C_OBJS) $(CXX_OBJS))
    
    .DEFAULT_GOAL := $(BUILD_DIR)/ssh-tools
    
    ## Automatic dependency building
    DEPFLAGS = -MT $@ -MMD -MP -MF $(BUILD_DIR)/$*.Td
    DEPFILES := $(OBJS:%.o=%.d)
    
    ## Dummy target for $(DEPFILES) when they are not present.
    $(DEPFILES):
    ## Use wildcard so that nonexisitent dep files are ignored.
    include $(wildcard $(DEPFILES))
    
    ## Build rules
    .SECONDEXPANSION:
    
    # Disable implict pattern
    $(BUILD_DIR)/ssh-tools: $(OBJS)
    	$(CXX) $(LDFLAGS) $(LIBS) $^ -o $@
    
    $(BUILD_DIR)/%.o: %.c $(BUILD_DIR)/%.d $$(wildcard %.h) Makefile
    	$(CC) -std=c11 -c $(CFLAGS) $(DEPFLAGS) -o $@ $<
    	mv -f $(BUILD_DIR)/$*.Td $(BUILD_DIR)/$*.d && touch $@
    
    $(BUILD_DIR)/%.o: %.cc $(BUILD_DIR)/%.d $$(wildcard %.h) $$(wildcard %.hpp) Makefile
    	$(CXX) -std=c++17 -c $(CXXFLAGS) $(CFLAGS) $(DEPFLAGS) -o $@ $<
    	mv -f $(BUILD_DIR)/$*.Td $(BUILD_DIR)/$*.d && touch $@
    
    compile_flags.txt: Makefile
    	echo '-xc++' $(CXXFLAGS) $(CFLAGS) | sed 's/-I/-I /g' | xargs -n1 echo | tee $@
    
    compile_commands.json: Makefile
    	rm -rf /tmp/ssh-tools_build_dir/
    	mkdir -p /tmp/ssh-tools_build_dir/
    	BUILD_DIR=/tmp/ssh-tools_build_dir/ DEBUG=true compiledb make -j $(shell nproc)
    	rm -rf /tmp/ssh-tools_build_dir/
    
    ### Move from run_all_builds.sh to further parallel the builds
    all_builds: release_build
    
    debug_build:
    	mkdir -p $@
    	$(MAKE) BUILD_DIR=$@ DEBUG=true
    
    release_build:
    	mkdir -p $@
    	$(MAKE) BUILD_DIR=$@ DEBUG=false
    
    install: $(BUILD_DIR)/ssh-tools
    	cp -f $(BUILD_DIR)/ssh-tools $(TARGET_DIR)/bin/
    
    install_release_build: release_build
    	$(MAKE) BUILD_DIR=release_build DEBUG=false install
    
    clean:
    	rm -rf $(OBJS) $(BUILD_DIR)/ssh-tools *_build/
    
    .PHONY: all_builds debug_build release_build install install_release_build clean
    ```

    This `Makefile` is from [NobodyXu/ssh-tools](github.com/NobodyXu/ssh-tools).

