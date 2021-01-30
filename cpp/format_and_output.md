 1. [fmtlib/fmt](https://github.com/fmtlib/fmt)
    
    > Features
    > --------
    > 
    > * Simple `format API <https://fmt.dev/latest/api.html>`_ with positional arguments
    >   for localization
    > * Implementation of `C++20 std::format
    >   <https://en.cppreference.com/w/cpp/utility/format>`__
    > * `Format string syntax <https://fmt.dev/latest/syntax.html>`_ similar to Python's
    >   `format <https://docs.python.org/3/library/stdtypes.html#str.format>`_
    > * Fast IEEE 754 floating-point formatter with correct rounding, shortness and
    >   round-trip guarantees
    > * Safe `printf implementation
    >   <https://fmt.dev/latest/api.html#printf-formatting>`_ including the POSIX
    >   extension for positional arguments
    > * Extensibility: `support for user-defined types
    >   <https://fmt.dev/latest/api.html#formatting-user-defined-types>`_
    > * High performance: faster than common standard library implementations of
    >   ``(s)printf``, iostreams, ``to_string`` and ``to_chars``, see `Speed tests`_
    >   and `Converting a hundred million integers to strings per second
    >   <http://www.zverovich.net/2020/06/13/fast-int-to-string-revisited.html>`_
    > * Small code size both in terms of source code with the minimum configuration
    >   consisting of just three files, ``core.h``, ``format.h`` and ``format-inl.h``,
    >   and compiled code; see `Compile time and code bloat`_
    > * Reliability: the library has an extensive set of `tests
    >   <https://github.com/fmtlib/fmt/tree/master/test>`_ and is `continuously fuzzed
    >   <https://bugs.chromium.org/p/oss-fuzz/issues/list?colspec=ID%20Type%20
    >   Component%20Status%20Proj%20Reported%20Owner%20Summary&q=proj%3Dfmt&can=1>`_
    > * Safety: the library is fully type safe, errors in format strings can be
    >   reported at compile time, automatic memory management prevents buffer overflow
    >   errors
    > * Ease of use: small self-contained code base, no external dependencies,
    >   permissive MIT `license
    >   <https://github.com/fmtlib/fmt/blob/master/LICENSE.rst>`_
    > * `Portability <https://fmt.dev/latest/index.html#portability>`_ with
    >   consistent output across platforms and support for older compilers
    > * Clean warning-free codebase even on high warning levels such as
    >   ``-Wall -Wextra -pedantic``
    > * Locale-independence by default
    > * Optional header-only configuration enabled with the ``FMT_HEADER_ONLY`` macro
    > 
    > See the `documentation <https://fmt.dev>`_ for more details.
