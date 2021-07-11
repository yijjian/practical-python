# pcost.py
#
# Exercise 1.27
import sys


def portfolio_cost(filename):
    import csv
    with open(filename) as f:
        total = 0
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                name, shares, price = row[0], int(row[1]), float(row[2])
            except:
                print('Missing data')
            total += shares * price
        return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)