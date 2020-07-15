# pcost.py
#
# Exercise 1.27
import sys
import csv
from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    total = 0
    for row in portfolio:
        total += int(row['shares']) * float(row['price'])
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)


