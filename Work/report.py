# report.py
#
# Exercise 2.4
import csv
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
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            holding = {'name':record['name'], 'shares':int(record['shares']), 'price':float(record['price'])}
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except Exception:
                print('It\'s over')
    return prices

def make_report(portfolio, prices):
    report = []

    for stk in portfolio:
        report.append((stk['name'],stk['shares'],prices[stk['name']],prices[stk['name']] - stk['price']))
    return report

    
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

print('{:>16} {:>16} {:>16} {:>16}'.format('Name','Shares','Price','Change'))
value = ' -'
print(f'{value * 8} {value * 8} {value * 8} {value * 8}')
for name, shares, price, change in report:
    price = '$' + str('%0.2f'% price)
    print(f'{name:>16s} {shares:>16d} {price:>16} {change:>16.2f}')

'''
print('{:>16} {:>16} {:>16} {:>16}'.format('Name','Shares','Price','Change'))
value = ' -'
print(f'{value * 8} {value * 8} {value * 8} {value * 8}')
for stk in portfolio:
    print('{name:>16} {shares:>16} {price:>16.2f} {change:>16.2f}'.format_map(stk))
'''
