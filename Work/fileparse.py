# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        if delimiter:
            rows = csv.reader(f, delimiter=delimiter)
        else:
            rows = csv.reader(f)

        if has_headers == True:

            # Read the file headers
            headers = next(rows)

            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []

            
            records = []
            for row in rows:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                if not row:    # Skip rows with no data
                    continue
                if indices:
                    row = [row[index] for index in indices]
                    
                record = dict(zip(headers, row))
                records.append(record)

        else:
            records = []
            for row in rows:
                if types:
                    row = tuple([func(val) for func, val in zip(types, row)])
                if not row:    # Skip rows with no data
                    continue
                records.append(row)
            

    return records
