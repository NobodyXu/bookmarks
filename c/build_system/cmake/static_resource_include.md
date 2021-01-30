 1. Retrieved from [Proof Of Concept: Re-implementing Qt moc using libclang](https://woboq.com/blog/moc-with-clang.html)
    
    ```
    file(GLOB BUILTINS_HEADERS "${LLVM_BIN_DIR}/../lib/clang/${LLVM_VERSION}/include/*.h")
    foreach(BUILTIN_HEADER ${BUILTINS_HEADERS})
        file(READ ${BUILTIN_HEADER} BINARY_DATA HEX)
        string(REGEX REPLACE "(..)" "\\\\x\\1" BINARY_DATA "${BINARY_DATA}")
        string(REPLACE "${LLVM_BIN_DIR}/../lib/clang/${LLVM_VERSION}/include/" 
                       "/builtins/" FN "${BUILTIN_HEADER}")
        set(EMBEDDED_DATA "${EMBEDDED_DATA} { \"${FN}\" , \"${BINARY_DATA}\" } , ")
    endforeach()
    configure_file(embedded_includes.h.in embedded_includes.h)
    ```
