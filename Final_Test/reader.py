'''
    Reads and returns the values present in a column as a list
'''
import csv

def read_col(filename, col_name, col_type):
    values = list()
    with open(filename) as FH:
        rows = csv.reader(FH)
        headers = next(rows)
        col_idx = headers.index(col_name)
        for row in rows:
            #wins = int(row[col_idx])
            val = col_type(row[col_idx])
            values.append(val)

    return values
