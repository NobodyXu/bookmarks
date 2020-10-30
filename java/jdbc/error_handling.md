 1. [How to catch a specific exception in JDBC?](https://stackoverflow.com/questions/1988570/how-to-catch-a-specific-exception-in-jdbc)
    
    TL;DR:
    
    Use `String SQLException.getSQLState()` and check the return value against:
    
    > - 02: no data
    > - 07: dynamic SQL error
    > - 08: connection exception
    > - 0A: feature not supported
    > - 21: cardinality violation
    > - 22: data exception
    > - 23: integrity constraint violation
    > - 24: invalid cursor state
    > - 25: invalid transaction state
    > - 26: invalid SQL statement name
    > - 28: invalid authorization specification
    > - 2B: dependent privilege descriptors still exist
    > - 2C: invalid character set name
    > - 2D: invalid transaction termination
    > - 2E: invalid connection name
    > - 33: invalid SQL descriptor name
    > - 34: invalid cursor name
    > - 35: invalid condition number
    > - 3C: ambiguous cursor name
    > - 3D: invalid catalog name
    > - 3F: invalid schema name
    
    Or this, a more detailed description:
    
    ```
    +----+-----------------------------------------------------------+-----+--------------------------------------------------------------+
    | Class and class description                                    | Subclass and subclass description                                  |
    +----+-----------------------------------------------------------+-----+--------------------------------------------------------------+
    | 00 | Successful completion                                     | 000 | No subclass                                                  |
    | 01 | Warning                                                   | 000 | No subclass                                                  |
    | 01 | Warning                                                   | 001 | Cursor operation conflict                                    |
    | 01 | Warning                                                   | 002 | Disconnect error                                             |
    | 01 | Warning                                                   | 003 | Null value eliminated in set function                        |
    | 01 | Warning                                                   | 004 | String data, right truncation                                |
    | 01 | Warning                                                   | 005 | Insufficient item descriptor areas                           |
    | 01 | Warning                                                   | 006 | Privilege not revoked                                        |
    | 01 | Warning                                                   | 007 | Privilege not granted                                        |
    | 01 | Warning                                                   | 009 | Search condition too long for information schema             |
    | 01 | Warning                                                   | 00A | Query expression too long for information schema             |
    | 01 | Warning                                                   | 00B | Default value too long for information schema                |
    | 01 | Warning                                                   | 00C | Result sets returned                                         |
    | 01 | Warning                                                   | 00D | Additional result sets returned                              |
    | 01 | Warning                                                   | 00E | Attempt to return too many result sets                       |
    | 01 | Warning                                                   | 00F | Statement too long for information schema                    |
    | 01 | Warning                                                   | 012 | Invalid number of conditions                                 |
    | 01 | Warning                                                   | 02F | Array data, right truncation                                 |
    | 02 | No data                                                   | 000 | No subclass                                                  |
    | 02 | No data                                                   | 001 | No additional result sets returned                           |
    | 07 | Dynamic SQL Error                                         | 000 | No subclass                                                  |
    | 07 | Dynamic SQL Error                                         | 001 | Using clause does not match dynamic parameter specifications |
    | 07 | Dynamic SQL Error                                         | 002 | Using clause does not match target specifications            |
    | 07 | Dynamic SQL Error                                         | 003 | Cursor specification cannot be executed                      |
    | 07 | Dynamic SQL Error                                         | 004 | Using clause required for dynamic parameters                 |
    | 07 | Dynamic SQL Error                                         | 005 | Prepared statement not a cursor specification                |
    | 07 | Dynamic SQL Error                                         | 006 | Restricted data type attribute violation                     |
    | 07 | Dynamic SQL Error                                         | 007 | Using clause required for result fields                      |
    | 07 | Dynamic SQL Error                                         | 008 | Invalid descriptor count                                     |
    | 07 | Dynamic SQL Error                                         | 009 | Invalid descriptor index                                     |
    | 07 | Dynamic SQL Error                                         | 00B | Data type transform function violation                       |
    | 07 | Dynamic SQL Error                                         | 00C | Undefined DATA value                                         |
    | 07 | Dynamic SQL Error                                         | 00D | Invalid DATA target                                          |
    | 07 | Dynamic SQL Error                                         | 00E | Invalid LEVEL value                                          |
    | 07 | Dynamic SQL Error                                         | 00F | Invalid DATETIME_INTERVAL_CODE                               |
    | 08 | Connection exception                                      | 000 | No subclass                                                  |
    | 08 | Connection exception                                      | 001 | SQL-client unable to establish SQL-connection                |
    | 08 | Connection exception                                      | 002 | Connection name in use                                       |
    | 08 | Connection exception                                      | 003 | Connection does not exist                                    |
    | 08 | Connection exception                                      | 004 | SQL-server rejected establishment of SQL-connection          |
    | 08 | Connection exception                                      | 006 | Connection failure                                           |
    | 08 | Connection exception                                      | 007 | Transaction resolution unknown                               |
    | 09 | Triggered action exception                                | 000 | No subclass                                                  |
    | 0A | Feature not supported                                     | 000 | No subclass                                                  |
    | 0A | Feature not supported                                     | 001 | Multiple server transactions                                 |
    | 0D | Invalid target type specification                         | 000 | No subclass                                                  |
    | 0E | Invalid schema name list specification                    | 000 | No subclass                                                  |
    | 0F | Locator exception                                         | 000 | No subclass                                                  |
    | 0F | Locator exception                                         | 001 | Invalid specification                                        |
    | 0L | Invalid grantor                                           | 000 | No subclass                                                  |
    | 0M | Invalid SQL-invoked procedure reference                   | 000 | No subclass                                                  |
    | 0P | Invalid role specification                                | 000 | No subclass                                                  |
    | 0S | Invalid transform group name specification                | 000 | No subclass                                                  |
    | 0T | Target table disagrees with cursor specification          | 000 | No subclass                                                  |
    | 0U | Attempt to assign to non-updatable column                 | 000 | No subclass                                                  |
    | 0V | Attempt to assign to ordering column                      | 000 | No subclass                                                  |
    | 0W | Prohibited statement encountered during trigger execution | 000 | No subclass                                                  |
    | 0W | Prohibited statement encountered during trigger execution | 001 | Modify table modified by data change delta table             |
    | 0Z | Diagnostics exception                                     | 000 | No subclass                                                  |
    | 0Z | Diagnostics exception                                     | 001 | Maximum number of stacked diagnostics areas exceeded         |
    | 21 | Cardinality violation                                     | 000 | No subclass                                                  |
    | 22 | Data exception                                            | 000 | No subclass                                                  |
    | 22 | Data exception                                            | 001 | String data, right truncation                                |
    | 22 | Data exception                                            | 002 | Null value, no indicator parameter                           |
    | 22 | Data exception                                            | 003 | Numeric value out of range                                   |
    | 22 | Data exception                                            | 004 | Null value not allowed                                       |
    | 22 | Data exception                                            | 005 | Error in assignment                                          |
    | 22 | Data exception                                            | 006 | Invalid interval format                                      |
    | 22 | Data exception                                            | 007 | Invalid datetime format                                      |
    | 22 | Data exception                                            | 008 | Datetime field overflow                                      |
    | 22 | Data exception                                            | 009 | Invalid time zone displacement value                         |
    | 22 | Data exception                                            | 00B | Escape character conflict                                    |
    | 22 | Data exception                                            | 00C | Invalid use of escape character                              |
    | 22 | Data exception                                            | 00D | Invalid escape octet                                         |
    | 22 | Data exception                                            | 00E | Null value in array target                                   |
    | 22 | Data exception                                            | 00F | Zero-length character string                                 |
    | 22 | Data exception                                            | 00G | Most specific type mismatch                                  |
    | 22 | Data exception                                            | 00H | Sequence generator limit exceeded                            |
    | 22 | Data exception                                            | 00P | Interval value out of range                                  |
    | 22 | Data exception                                            | 00Q | Multiset value overflow                                      |
    | 22 | Data exception                                            | 010 | Invalid indicator parameter value                            |
    | 22 | Data exception                                            | 011 | Substring error                                              |
    | 22 | Data exception                                            | 012 | Division by zero                                             |
    | 22 | Data exception                                            | 013 | Invalid preceding or following size in window function       |
    | 22 | Data exception                                            | 014 | Invalid argument for NTILE function                          |
    | 22 | Data exception                                            | 015 | Interval field overflow                                      |
    | 22 | Data exception                                            | 016 | Invalid argument for NTH_VALUE function                      |
    | 22 | Data exception                                            | 018 | Invalid character value for cast                             |
    | 22 | Data exception                                            | 019 | Invalid escape character                                     |
    | 22 | Data exception                                            | 01B | Invalid regular expression                                   |
    | 22 | Data exception                                            | 01C | Null row not permitted in table                              |
    | 22 | Data exception                                            | 01E | Invalid argument for natural logarithm                       |
    | 22 | Data exception                                            | 01F | Invalid argument for power function                          |
    | 22 | Data exception                                            | 01G | Invalid argument for width bucket function                   |
    | 22 | Data exception                                            | 01H | Invalid row version                                          |
    | 22 | Data exception                                            | 01S | Invalid XQuery regular expression                            |
    | 22 | Data exception                                            | 01T | Invalid XQuery option flag                                   |
    | 22 | Data exception                                            | 01U | Attempt to replace a zero-length string                      |
    | 22 | Data exception                                            | 01V | Invalid XQuery replacement string                            |
    | 22 | Data exception                                            | 01W | Invalid row count in fetch first clause                      |
    | 22 | Data exception                                            | 01X | Invalid row count in result offset clause                    |
    | 22 | Data exception                                            | 020 | Invalid period value                                         |
    | 22 | Data exception                                            | 021 | Character not in repertoire                                  |
    | 22 | Data exception                                            | 022 | Indicator overflow                                           |
    | 22 | Data exception                                            | 023 | Invalid parameter value                                      |
    | 22 | Data exception                                            | 024 | Unterminated C string                                        |
    | 22 | Data exception                                            | 025 | Invalid escape sequence                                      |
    | 22 | Data exception                                            | 026 | String data, length mismatch                                 |
    | 22 | Data exception                                            | 027 | Trim error                                                   |
    | 22 | Data exception                                            | 029 | Noncharacter in UCS string                                   |
    | 22 | Data exception                                            | 02D | Null value substituted for mutator subject parameter         |
    | 22 | Data exception                                            | 02E | Array element error                                          |
    | 22 | Data exception                                            | 02F | Array data, right truncation                                 |
    | 22 | Data exception                                            | 02G | Invalid repeat argument in sample clause                     |
    | 22 | Data exception                                            | 02H | Invalid sample size                                          |
    | 23 | Integrity constraint violation                            | 000 | No subclass                                                  |
    | 23 | Integrity constraint violation                            | 001 | Restrict violation                                           |
    | 24 | Invalid cursor state                                      | 000 | No subclass                                                  |
    | 25 | Invalid transaction state                                 | 000 | No subclass                                                  |
    | 25 | Invalid transaction state                                 | 001 | Active SQL-transaction                                       |
    | 25 | Invalid transaction state                                 | 002 | Branch transaction already active                            |
    | 25 | Invalid transaction state                                 | 003 | Inappropriate access mode for branch transaction             |
    | 25 | Invalid transaction state                                 | 004 | Inappropriate isolation level for branch transaction         |
    | 25 | Invalid transaction state                                 | 005 | No active SQL-transaction for branch transaction             |
    | 25 | Invalid transaction state                                 | 006 | Read-only SQL-transaction                                    |
    | 25 | Invalid transaction state                                 | 007 | Schema and data statement mixing not supported               |
    | 25 | Invalid transaction state                                 | 008 | Held cursor requires same isolation level                    |
    | 26 | Invalid SQL statement name                                | 000 | No subclass                                                  |
    | 27 | Triggered data change violation                           | 000 | No subclass                                                  |
    | 27 | Triggered data change violation                           | 001 | Modify table modified by data change delta table             |
    | 28 | Invalid authorization specification                       | 000 | No subclass                                                  |
    | 2B | Dependent privilege descriptors still exist               | 000 | No subclass                                                  |
    | 2C | Invalid character set name                                | 000 | No subclass                                                  |
    | 2C | Invalid character set name                                | 001 | Cannot drop SQL-session default character set                |
    | 2D | Invalid transaction termination                           | 000 | No subclass                                                  |
    | 2E | Invalid connection name                                   | 000 | No subclass                                                  |
    | 2F | SQL routine exception                                     | 000 | No subclass                                                  |
    | 2F | SQL routine exception                                     | 002 | Modifying SQL-data not permitted                             |
    | 2F | SQL routine exception                                     | 003 | Prohibited SQL-statement attempted                           |
    | 2F | SQL routine exception                                     | 004 | Reading SQL-data not permitted                               |
    | 2F | SQL routine exception                                     | 005 | Function executed no return statement                        |
    | 2H | Invalid collation name                                    | 000 | No subclass                                                  |
    | 30 | Invalid SQL statement identifier                          | 000 | No subclass                                                  |
    | 33 | Invalid SQL descriptor name                               | 000 | No subclass                                                  |
    | 34 | Invalid cursor name                                       | 000 | No subclass                                                  |
    | 35 | Invalid condition number                                  | 000 | No subclass                                                  |
    | 36 | Cursor sensitivity exception                              | 000 | No subclass                                                  |
    | 36 | Cursor sensitivity exception                              | 001 | request rejected                                             |
    | 36 | Cursor sensitivity exception                              | 002 | request failed                                               |
    | 38 | External routine exception                                | 000 | No subclass                                                  |
    | 38 | External routine exception                                | 001 | Containing SQL not permitted                                 |
    | 38 | External routine exception                                | 002 | Modifying SQL-data not permitted                             |
    | 38 | External routine exception                                | 003 | Prohibited SQL-statement attempted                           |
    | 38 | External routine exception                                | 004 | Reading SQL-data not permitted                               |
    | 39 | External routine invocation exception                     | 000 | No subclass                                                  |
    | 39 | External routine invocation exception                     | 004 | Null value not allowed                                       |
    | 3B | Savepoint exception                                       | 000 | No subclass                                                  |
    | 3B | Savepoint exception                                       | 001 | Invalid specification                                        |
    | 3B | Savepoint exception                                       | 002 | Too many                                                     |
    | 3C | Ambiguous cursor name                                     | 000 | No subclass                                                  |
    | 3D | Invalid catalog name                                      | 000 | No subclass                                                  |
    | 3F | Invalid schema name                                       | 000 | No subclass                                                  |
    | 40 | Transaction rollback                                      | 000 | No subclass                                                  |
    | 40 | Transaction rollback                                      | 001 | Serialization failure                                        |
    | 40 | Transaction rollback                                      | 002 | Integrity constraint violation                               |
    | 40 | Transaction rollback                                      | 003 | Statement completion unknown                                 |
    | 40 | Transaction rollback                                      | 004 | Triggered action exception                                   |
    | 42 | Syntax error or access rule violation                     | 000 | No subclass                                                  |
    | 44 | With check option violation                               | 000 | No subclass                                                  |
    | HZ | Remote database access                                    | 000 | No subclass                                                  |
    +----+-----------------------------------------------------------+-----+--------------------------------------------------------------+
    ```
    
    The data above is retrieved from [ISO - Database Language SQL](http://www.contrib.andrew.cmu.edu/~shadow/sql/sql1992.txt)
