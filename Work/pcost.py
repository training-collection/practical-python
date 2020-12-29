# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    '''
    Calculates total cost of share portfolio
    Adusted to use csv package
    Adjusted to be able to call a fileneame from the terminal
    '''
    total_cost = 0.0
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    return total_cost

'''
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
  
print('Total cost:', cost)
'''
