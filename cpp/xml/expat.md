## libexpat, an SAX model for reading in XML file

 1. [Using Expat]
 2. [Geting xml data using xml parser expat]
 3. [expat.h]
 4. expat example code snippet 1:
 
 ```
 /**
 * clang++ -std=c++17 -lexpat expat_example.cc -O3 -s
 */
 
 #include <err.h>
 
 #include <cstdint>
 #include <cstdio>
 #include <memory>
 #include <type_traits>
 
 #include <expat.h>
 
 struct XML_Parser_Deleter {
     void operator () (XML_Parser p) const noexcept
     {
         XML_ParserFree(p);
     }
 };
 using XML_Parser_Ptr = std::unique_ptr<std::decay_t<decltype(*std::declval<XML_Parser>())>, XML_Parser_Deleter>;
 
 void XML_Parse_Wrapper(XML_Parser p, char *buffer, std::size_t len, int finished) noexcept
 {
     if (XML_Parse(p, buffer, len, finished) == XML_STATUS_ERROR)
         errx(1, "XML_Parse failed: %s", XML_ErrorString(XML_GetErrorCode(p)));
 }
 
 int main(int argc, char* argv[])
 {
     auto parser = XML_Parser_Ptr{XML_ParserCreate(nullptr /* optionally, you can set this param to "utf-8" or "utf-16" */)};
     if (!parser)
         errx(1, "Failed to create XML parser");
 
     std::uint64_t depth = 0;
 
     XML_SetElementHandler(parser.get(), 
     [](void *data, const char *element, const char **attr) noexcept
     {
         auto &depth = *static_cast<std::uint64_t*>(data);
 
         for (std::size_t i = 0; i != depth; ++i)
             std::putchar(' ');
 
         std::printf("<%s", element);
         for (std::size_t i = 0; attr[i]; i += 2)
             std::printf(" %s=\"%s\"", attr[i], attr[i + 1]);
         std::fputs(">", stdout);
 
         depth += 4;
     }, [](void *data, const char *element) noexcept
     {
         auto &depth = *static_cast<std::uint64_t*>(data);
         depth -= 4;
         std::printf("</%s>", element);
     });
     XML_SetUserData(parser.get(), &depth);
 
     XML_SetCharacterDataHandler(parser.get(), 
     [](void *data, const XML_Char *s, int len) noexcept
     {
         /**
          * NOTE:
          * 
          * Some xml might contain '\n' character data
          * - at the begining of a xml node with child node;
          * - at the end of node.
          * 
          * Check https://www.speedtest.net/speedtest-config.php for example.
          */
         std::fwrite(s, sizeof(XML_Char), len, stdout);
     });
 
     char buffer[1024];
     for (; !std::feof(stdin); ) {
         auto size = fread(buffer, 1, sizeof(buffer), stdin);
         if (std::ferror(stdin))
             err(1, "std::fread failed");
 
         XML_Parse_Wrapper(parser.get(), buffer, size, 0);
     }
 
     XML_Parse_Wrapper(parser.get(), nullptr, 0, 1);
 
     return 0;
 }
 ```
 5. `XML_ParserReset(XML_Parser parser, const XML_Char *encoding)` can be used to reset `XML_Parser`
 to a usable state after `XML_Parse(parser, buffer, size, 1 /* signature parsing is done */)`.
 
 After reset, all handlers are cleared from the parser.
 
[Using Expat]: https://www.xml.com/pub/a/1999/09/expat/index.html
[Geting xml data using xml parser expat]: https://stackoverflow.com/questions/609376/geting-xml-data-using-xml-parser-expat
[expat.h]: https://github.com/libexpat/libexpat/blob/master/expat/lib/expat.h
