 - Specify condition in `count`:
   
   If using Postgres or SQLite, you can use the Filter clause to improve readability:


   ```sql
   SELECT
     COUNT(1) FILTER (WHERE cond),
     COUNT(1) FILTER (WHERE cond)
   FROM ...
   ```

   Otherwise:

   ```
   SELECT SUM(CASE WHEN cond THEN 1 ELSE 0 END),
          SUM(CASE WHEN cond THEN 1 ELSE 0 END)
      FROM SomeTable
   ```

   or:

   ```
   SELECT COUNT(case when cond then 1 else null end)
     FROM ...
   ```
   
   From [this stackoverflow question](https://stackoverflow.com/questions/1400078/is-it-possible-to-specify-condition-in-count).
 - Postgres support `generate_series` to generate integers in the range.
 - [Postgres sorting algorithms](https://madusudanan.com/blog/all-you-need-to-know-about-sorting-in-postgres/)
   
    - External merge: Slowest, for tables too large to fit in the memory.
    - Quick sort: Faster than external merge, used if the table fits in the memory.
    - Top-N heapsort: Faster than quicksort,  used when `LIMIT` is specified with `ORDER BY`.
    - Sorting using indexes: Fastest, just lookup, no sorting.
 - SQLite support `INSERT OT IGNORE INTO ...` to insert only if the element is not present.
   It needs to be used with adding `UNIQUE` constraint to the table.
