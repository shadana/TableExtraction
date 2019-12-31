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

<b>Instructions for execution:</b>
1. The excel files are first unmerged to remove the merged cells of the excel sheets. This is done by Unmerged.py. The output is received as <filename>_unmerged.
  
2. The merged and unmerged files are used to extract the tables. This is done by TableExtraction.py. This prints out the tables and the schema matches if multiple tables are present. 

For the excel files in the Test folders, every file already has it corresponding unmerged file which can be used to extract tables. For new excels, this step needs to be done before extraction.
