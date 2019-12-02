import pandas as pd
import numpy as np

def printTable(table, headerRows, header):
    print('----------------------------------------------------------')

    for column in header:
        print(column + '\t'),

    print('')
    print('----------------------------------------------------------')

    rows = 0
    for index_row, row in table.iterrows():
        if rows != headerRows:
            rows = rows + 1
            continue
        for index_col, col in enumerate(row):
                print(str(col) + '\t'),
        print('')

    print('----------------------------------------------------------')
    print('')
    print('')


