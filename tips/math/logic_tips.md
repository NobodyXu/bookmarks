 - [How to convert any logic expression to CNF?](https://stackoverflow.com/questions/53795696/convert-formula-to-cnf-python)
   
   ```python3
   from sympy.logic.boolalg import to_cnf
   from sympy.abc import A, B, D
   to_cnf(~(A | B) | D)
   ```
