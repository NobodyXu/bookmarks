 1. [Savepoint Notes](https://docs.oracle.com/cd/B12037_01/java.101/b10979/jdbcversion.htm#:~:text=When%20a%20transaction%20is%20committed,after%20the%20savepoint%20in%20question.)
    
    > - When a transaction is committed or rolled back, all savepoints created in that transaction are automatically released and become invalid.
    > - Rolling a transaction back to a savepoint automatically releases and makes invalid any savepoints created after the savepoint in question.
    
