# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv
def portfolio_cost(filename):
    total_cost = 0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            nshares = int(record['shares'])
            price = float(record['price'])
            total_cost += nshares * price
    return total_cost

def read_portfolio(filename):
    portfolio = parse_csv(filename, has_headers=True)
    return portfolio

def read_prices(filename):
    prices = parse_csv(filename, has_headers=False)
    return prices


def make_report(portfolio, prices):
    report = []

    for stk in portfolio:
        report.append((stk['name'],stk['shares'],prices[stk['name']],prices[stk['name']] - stk['price']))
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)



'''
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
print_report(report)
'''




