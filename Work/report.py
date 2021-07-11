# report.py
#
# Exercise 2.4
import sys
import csv
from pprint import pprint


def portfolio_cost(filename):
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


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        heads = next(rows)
        for row in rows:
            holding = {'name': row[0], 'shares':int(row[1]), 'price':float(row[2])}
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        prices = {}
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                pass
    return prices


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/prices.csv'
prices = read_prices(filename)
pprint(prices)
print(prices['AA'])
print(prices['AXP'])

