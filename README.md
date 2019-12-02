# TableExtraction

To extract the tables present in the excel sheets and print them in SQLlite format.

<b>Unmerged.py</b>
The tables may contain merged cells before using them to extract the tables, the cells must be unmerged. 
Usage - python Unmerge.py <MergedExcel>
This gives the output of the excel with the cells unmerged.

<b>TableExtraction.py</b>
The tables are extracted from the Excel sheets and the column names are schema matched and printed. (If there is just one table, the schema match is empty). This internally uses the following:
SchemaMatching.py - for matching columns of tables.
PrintTable.py - for printing the tables in SQLlite.
Usage - python TableExtraction.py <UnmergedExcel> <MergedExcel>

