# TableExtraction

To extract the tables present in the excel sheets and print them in SQLlite format.

#Unmerged.py 
The tables may contain merged cells before using them to extract the tables, the cells must be unmerged. 
Usage - python Unmerge.py <MergedExcel>
This gives the output of the excel with the cells unmerged.

#TableExtraction.py
The tables are extracted from the Excel sheets and the column names are schema matched and printed. (If there is just one table, the schema match is empty)
Usage - python TableExtraction.py <UnmergedExcel> <MergedExcel>
