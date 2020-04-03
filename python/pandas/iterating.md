 1. [How to iterate over rows in a DataFrame in Pandas?]
  
 TL;DR
 
 > Do you want to print a DataFrame? Use DataFrame.to_string().
 > 
 > Do you want to compute something? In that case, search for methods in this order (list modified from here):
 > 
 > Vectorization
 > Cython routines
 > List Comprehensions (vanilla for loop)
 > DataFrame.apply(): i)  Reductions that can be performed in cython, ii) Iteration in python space
 > DataFrame.itertuples() and iteritems()
 > DataFrame.iterrows()
 
 In addition to the answer, there's this one:
 
   [numpy vectorization is faster than pandas vectorization]
 
 2. [A Beginner’s Guide to Optimizing Pandas (loop) Code for Speed]
 
[How to iterate over rows in a DataFrame in Pandas?]: https://stackoverflow.com/a/55557758/8375400
[A Beginner’s Guide to Optimizing Pandas (loop) Code for Speed]: https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6
[numpy vectorization is faster than pandas vectorization]: https://stackoverflow.com/a/60836700/8375400
