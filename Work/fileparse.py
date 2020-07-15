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
                headers = indices
            else:
                indices = []

            
            records = []
            for row in rows:
                if types:
                    try:
                        row = [func(val) for func, val in zip(types, row)]
                    except ValueError as e:
                        pass
                if not row:    # Skip rows with no data
                    continue
                if indices:
                    row = [row[index] for index in indices]
                    print(row)
                    
                record = dict(zip(headers, row))
                records.append(record)

        else:
            if select and has_headers == False:
                raise RuntimeError('select argument requires column headers')
            records = {}
            for i, row in enumerate(rows, start=1):
                if types:
                    try:
                        row = tuple([func(val) for func, val in zip(types, row)])
                        name, price = row
                    except ValueError as e:
                        pass
                if not row:    # Skip rows with no data
                    continue
                records[name] = price
            

    return records
