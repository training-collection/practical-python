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