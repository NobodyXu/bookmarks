 1. [fmtlib/fmt](https://github.com/fmtlib/fmt)
    
    > Features
    > --------
    > 
    > * Simple [format API](https://fmt.dev/latest/api.html) with positional arguments
    >   for localization
    > * Implementation of C++20 [`std::format`](https://en.cppreference.com/w/cpp/utility/format)
    > * [Format string syntax](https://fmt.dev/latest/syntax.html) similar to [Python's format](https://docs.python.org/3/library/stdtypes.html#str.format)
    > * Fast IEEE 754 floating-point formatter with correct rounding, shortness and
    >   round-trip guarantees
    > * Safe [`printf` implementation](https://fmt.dev/latest/api.html#printf-formatting) including the POSIX
    >   extension for positional arguments
    > * Extensibility: [support for user-defined types](https://fmt.dev/latest/api.html#formatting-user-defined-types>)
    > * High performance: faster than common standard library implementations of
    >   `(s)printf`, `iostreams`, `to_string` and `to_chars`, see [Speed tests](https://github.com/fmtlib/fmt/blob/master/README.rst#speed-tests)
    >   and [Converting a hundred million integers to strings per second](http://www.zverovich.net/2020/06/13/fast-int-to-string-revisited.html)
    > * Small code size both in terms of source code with the minimum configuration
    >   consisting of just three files, `core.h`, `format.h` and `format-inl.h`,
    >   and compiled code; see [Compile time and code bloat](https://github.com/fmtlib/fmt/blob/master/README.rst#compile-time-and-code-bloat)
    > * Reliability: the library has an extensive set of [tests](https://github.com/fmtlib/fmt/tree/master/test) and is [continuously fuzzed](https://bugs.chromium.org/p/oss-fuzz/issues/list?colspec=ID%20Type%20Component%20Status%20Proj%20Reported%20Owner%20Summary&q=proj%3Dfmt&can=1)
    > * Safety: the library is fully type safe, errors in format strings can be
    >   reported at compile time, automatic memory management prevents buffer overflow
    >   errors
    > * Ease of use: small self-contained code base, no external dependencies,
    >   permissive [MIT license](https://github.com/fmtlib/fmt/blob/master/LICENSE.rst)
    > * [Portability](https://fmt.dev/latest/index.html#portability) with
    >   consistent output across platforms and support for older compilers
    > * Clean warning-free codebase even on high warning levels such as
    >   `-Wall -Wextra -pedantic`
    > * Locale-independence by default
    > * Optional header-only configuration enabled with the `FMT_HEADER_ONLY` macro
    > 
    > See the [documentation](https://fmt.dev) for more details.
 2. [{fmt} Compatibility with C++20 `std::format`](https://fmt.dev/dev/api.html#compatibility-with-c-20-std-format)
    
    > {fmt} implements nearly all of the C++20 formatting library with the following differences:
    > 
    > - Names are defined in the fmt namespace instead of std to avoid collisions with standard library implementations.
    > - Width calculation doesn’t use grapheme clusterization. The latter has been implemented in a separate branch but hasn’t been integrated yet.
    > - Chrono formatting doesn’t support C++20 date types since they are not provided by standard library implementations.
 3. [fmtlib/fmt: include/fmt/compile.h](https://github.com/fmtlib/fmt/blob/master/include/fmt/compile.h)
    
    This file contains functions/classes responsible for parsing format string at compile time.
 4. [gabime/spdlog](https://github.com/gabime/spdlog)
    
    Very fast, header-only/compiled, C++ logging library.
    
    Features:
     * Very fast (see [benchmarks](#benchmarks) below).
     * Headers only or compiled
     * Feature rich formatting, using the excellent [fmt](https://github.com/fmtlib/fmt) library.
     * Asynchronous mode (optional)
     * [Custom](https://github.com/gabime/spdlog/wiki/3.-Custom-formatting) formatting.
     * Multi/Single threaded loggers.
     * Various log targets:
         * Rotating log files.
         * Daily log files.
         * Console logging (colors supported).
         * syslog.
         * Windows debugger (```OutputDebugString(..)```)
         * Easily extendable with custom log targets  (just implement a single function in the [sink](https://github.com/gabime/spdlog/blob/master/include/spdlog/sinks/sink.h) interface).
     * Log filtering - log levels can be modified in runtime as well as in compile time.
     * Support for loading log levels from argv or from environment var.
     * [Backtrace](https://github.com/gabime/spdlog#backtrace-support) support - store debug messages in a ring buffer and display later on demand.
