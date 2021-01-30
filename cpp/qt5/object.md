 1. [Implicit Sharing](https://doc.qt.io/qt-5/implicit-sharing.html)
 2. [Implicit sharing iterator problem](https://doc.qt.io/qt-5/containers.html#implicit-sharing-iterator-problem)
 3. [The Property System](https://doc.qt.io/qt-5/properties.html)
 4. [Object Model](https://doc.qt.io/qt-5/object.html)
 5. [Timers](https://doc.qt.io/qt-5/timers.html)
 6. [Object Trees & Ownership](https://doc.qt.io/qt-5/objecttrees.html)
 7. [Creating Custom Qt Types](https://doc.qt.io/qt-5/custom-types.html)
 8. [How `QVariant` Works Internally?](https://stackoverflow.com/questions/4983819/how-qvariant-works-internally)
    
    Update:
    
    As of 2020, in the latest qt6 codebase, [`QVariant`](https://code.woboq.org/qt5/qtbase/src/corelib/kernel/qvariant.h.html#QVariant::d) no longer uses PIMPL.
    It has a `Private d` member, which is in turned defined directly in [`QVariant.h:Private`](https://code.woboq.org/qt5/qtbase/src/corelib/kernel/qvariant.h.html#QVariant::Private):
    
    ```c++
    struct Private
    {
        inline Private() noexcept : type(Invalid), is_shared(false), is_null(true)
        { data.ptr = nullptr; }
        // Internal constructor for initialized variants.
        explicit inline Private(uint variantType) noexcept
            : type(variantType), is_shared(false), is_null(false)
        {}
    #if QT_VERSION < QT_VERSION_CHECK(6, 0, 0)
        Private(const Private &other) noexcept
            : data(other.data), type(other.type),
              is_shared(other.is_shared), is_null(other.is_null)
        {}
        Private &operator=(const Private &other) noexcept = default;
    #endif
        union Data
        {
            char c;
            uchar uc;
            short s;
            signed char sc;
            ushort us;
            int i;
            uint u;
            long l;
            ulong ul;
            bool b;
            double d;
            float f;
            qreal real;
            qlonglong ll;
            qulonglong ull;
            QObject *o;
            void *ptr;
            PrivateShared *shared;
        } data;
        uint type : 30;
        uint is_shared : 1;
        uint is_null : 1;
    };
    ```
    
    This `struct Private` is `8 + 32 / 8` bytes long, which is 12 bytes in total.
