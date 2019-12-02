import os
import sys
import pandas as pd
import numpy as np
import math
from SchemaMatching import schemaMatch


__doc__ = '''Usage: TableExtraction.py <excel file1> <excelfile2>
    excel file1: the path for merged version of extraction excel file
    excel file2: the path for unmerged version of extraction excel file
    '''

unmerged_tables  = []
merged_tables = []
headers = []

def usage():
    print(__doc__)
    exit(-1)

def extractTable(unmerged, merged):
    
    start = -1
    end = 0
    start_row = -1
    num_rows = 0
    for index_row, row in unmerged.iterrows():
        if num_rows == 1 and end == -1 :
            end = unmerged.shape[1] - 1
            break
        for index_col, col in enumerate(row):
            if pd.isnull(col) != True:
                if start == -1:
                    start = index_col
                    start_row = index_row
                    end = -1
            if pd.isnull(col) == True and end == -1:
                end = index_col -1
                break
        num_rows = num_rows + 1
    
    if end == -1:
        end = unmerged.shape[1] - 1

    
#    print('start', start)
#    print('end', end)
#    print('start_row' , start_row)

    endRowTable = unmerged.iloc[start_row:, start:end+1]

    end_range = 0
    for index_row, row in endRowTable.iterrows():
        if(row.isna().all().all() == False):
            end_range = end_range + 1
        else:
            break


    end_row = start_row + end_range
#    print('end_row', end_row)
    unmerged_table = unmerged.iloc[start_row:end_row, start:end+1]
    merged_table = merged.iloc[start_row:end_row, start:end+1]

    unmerged_tables.append(unmerged_table)
    merged_tables.append(merged_table)

#    print(table)

    unmerged = unmerged.replace(unmerged.iloc[start_row:end_row, start:end+1], np.nan)
    merged = merged.replace(merged.iloc[start_row:end_row, start:end+1], np.nan)
    return unmerged


def tableExtraction(merged_path, unmerged_path):
    if not os.path.exists(merged_path):
        print(("Could not find the excel file: " % merged_path))
        return

    if not os.path.exists(merged_path):
        print(("Could not find the excel file: " % unmerged_path))
        return

    merged = pd.read_excel(merged_path, header = None)
    unmerged = pd.read_excel(unmerged_path, header = None)

    while(unmerged.isna().all().all() == False):
        df = extractTable(unmerged, merged)
        unmerged = df


def main():
    if 3 != len(sys.argv):
        usage()

    # actual input file
    merged_excel_file = sys.argv[1]

    # removed merged cells of the excel file
    unmerged_excel_file = sys.argv[2]

    tableExtraction(merged_excel_file, unmerged_excel_file)

#    print('unmerged')
#    print(unmerged_tables)
#    print('>>>>')
#
#    print('merged')
#    print(merged_tables)
#    print('>>>>')

    headers = schemaMatch(merged_tables, unmerged_tables)


if __name__ == '__main__':
    main()
