import pandas as pd
import numpy as np
import py_stringmatching as sm
from PrintTables import printTable

headers = []

def identifyHeaders(merged, unmerged):
    headerRows = 1
    for index_row, row in merged.iterrows():
        if(row.isna().any()):
            headerRows = headerRows + 1
        else:
            break

    rows = 0
    table_headers = [None] * len(merged.columns)

    for index_row, row in unmerged.iterrows():
        for index_col, col in enumerate(row):
            if table_headers[index_col] == None:
                table_headers[index_col] = str(col)
            else:
                table_headers[index_col] = str(table_headers[index_col]) + "_" + str(col)
        rows = rows + 1
        if(rows == headerRows):
            break

    printTable(unmerged, headerRows, table_headers)
    headers.append(table_headers)


def matchHeaders(headers):
    jac = sm.Jaccard()
    lev = sm.Levenshtein()
    oc = sm.OverlapCoefficient()
    
    i = 0
    j = 0
    
    header_len = len(headers)
    

    for i in range(0, header_len - 1):
        for first in headers[i]:
            j = i + 1
            if j == header_len:
                break
            for second in headers[j]:
#                print(first, '' , second, '')
#        i = i + 1
#        if(i == header_len):
#           continue
                x = first
                y = second
                delim_tok = sm.DelimiterTokenizer(delim_set=['_'])
                jacScore = jac.get_sim_score(delim_tok.tokenize(x), delim_tok.tokenize(y))
                levScore = lev.get_sim_score(x, y)
                ocScore = oc.get_sim_score(delim_tok.tokenize(x), delim_tok.tokenize(y))

                if(ocScore == 1 or levScore >= 0.5 or jacScore >= 0.5):
                    print(first +  ' of Table' + str(i+1) + ' and ' + second + ' of Table' + str(j+1) + ' matched')

def schemaMatch(merged_tables, unmerged_tables):
    for merged, unmerged in zip(merged_tables, unmerged_tables):
        identifyHeaders(merged, unmerged)

    print('############## The Schema match for these tables are ###################')
    print('')
    matchHeaders(headers)
    print('')
    
