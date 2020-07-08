# fileparse.py
#
# Exercise 3.3

import csv


    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        records = []
            if not row:
                continue
            record = dict(zip(headers, row))

    return records


            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = None


            
            for row in rows:
                if not row:
                    continue
                if indices:
                    row = [row[index] for index in indices]
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                record = dict(zip(headers, row))
                records.append(record)

            
        
        else:
            for row in rows:
                if not row:
                    continue
                if types:
                    record = tuple([func(val) for func, val in zip(types, row)])
                    records.append(record)
        return records


