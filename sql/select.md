 1. [The SQL SELECT INTO Statement][1]
 2. How to select table from a specific schema:
    
    Approach 1:
    
    ```
    SET search_path TO schema_name;
    SELECT * FROM database;
    ```
    
    Approach 2:
    
    ```
    SELECT * FROM schema_name.database;
    ```
    
[1]: https://www.w3schools.com/sql/sql_select_into.asp
