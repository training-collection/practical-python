# tableformat.py

class TableFormatter:
    def headings(self, headings):
        ''' make table headings '''
        raise NotImplementedError()

    def row(self, rowdata):
        ''' make single row of table data '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    ''' make a table in plain-text format '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    ''' output portfolio data in CSV format '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    ''' output portfolio data in HTML format '''
    def headings(self, headers):
        print('<tr>',end='')
        for h in headers:
            print(f'<th>{h}</th>',end='')
        print('</tr>')
    
    def row(self, rowdata):
        print(f'<tr>',end='')
        for row in rowdata:
            print(f'<td>{row}</td>',end='')
        print(f'</tr>')

# this class sets a user defined exception to distinguish it from python exceptions
class FormatError(Exception):
    pass

def create_formatter(name):
    ''' get the right formatter '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')

def print_table(objects, columns, formatter):
    ''' prints a formatted table to selected columns

    Args:   portfolio: output of report.read_portfolio('csv')
            columns: list of columns to appear in table
            formatter: output of create_formatter('xx') function in table_format
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [ str(getattr(obj, name)) for name in columns ]
        formatter.row(rowdata)
