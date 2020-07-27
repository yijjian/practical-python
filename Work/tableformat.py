class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()
class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10}', end=' ')
        print()



class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))



class HTMLTableFormatter(TableFormatter):

    def headings(self, headers):
        print('<tr><th>', end='')
        print('</th><th>'.join(headers), end='')
        print('</th></tr>')

    def row(self, rowdata):
        print('<tr><th>', end='')
        print('</th><th>'.join(rowdata), end='')
        print('</th></tr>')

class FormatError(Exception):
    pass


def create_formatter(name):
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknow table format %s' % name)

    if formatter:
        return formatter

def print_table(portfolio, columns, formatter):
    formatter.headings(columns)
    for stk in portfolio:
        rowdata = [getattr(stk, col) for col in columns]
        formatter.row(rowdata)
    
