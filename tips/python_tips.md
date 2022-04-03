 - `pigar` can be used to auto generate requirements.txt
 - Use the following snippet to import from non-package parent:
   
   ```
   import sys
   from os import path

   def import_from_parent(module_name: str):
       if module_name not in sys.modules:
           sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
           return __import__(module_name)
       else:
           return sys.modules[module_name]
   ```
