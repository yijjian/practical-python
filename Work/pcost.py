# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
    total = 0
    for num, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        print(row)
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            total += nshares * price
        except ValueError:
            print(f'Row {num}: Bad row: {row}')
    f.close
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)


