# report.py
#
# Exercise 2.4

import csv
import fileparse

'''
# reads the file in as a tuple
def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holiding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holiding)
    return portfolio
'''

def read_portfolio(filename):
    '''
    Reads file as a dictionary
    '''
    portfolio = fileparse.parse_csv(filename, has_headers=True, types=[str,int,float], select=['name','shares','price'])
    '''
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        d = {}
    
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                name = record['name']
                nshares = int(record['shares'])
                price = float(record['price']) 
                d = {'name': name, 'shares': nshares, 'price': price}
                portfolio.append(d)
    
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    '''
    return portfolio

def read_prices(filename):
    '''
    Reads file in as dictionary and handles NAN
    '''
    pricelist = fileparse.parse_csv(filename,has_headers=False,types=[str,float])
    prices = dict(pricelist)
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # note that there is no header
    
        dict = {}
        for row in rows:
            try:
                dict[row[0]] =  float(row[1])
            except IndexError:
                print("Could not parse", row)
    '''
    return prices


def print_report(portfolio_csv, prices_csv):
    '''
    Prints the report

    Previous exercises this was just coded into the
    end of the file, ex 3.1 changes it into a function
    '''
    #portfolio = read_portfolio(portfolio_csv)
    portfolio = fileparse.parse_csv(portfolio_csv, has_headers=True, types=[str,int,float], select=['name','shares','price'])

    inital_value = 0.0
    for s in portfolio:
        inital_value += s['shares']*s['price']

    #current_prices = read_prices(prices_csv)
    pricelist = fileparse.parse_csv(prices_csv,has_headers=False,types=[str,float])
    current_prices = dict(pricelist)
    
    final_value = 0.0
    for s in portfolio:
        final_value += s['shares']*current_prices[s['name']]
    
    profit = final_value - inital_value
    
    print('Inital value =', inital_value)
    print('Final value =', final_value)
    print('Profit/loss =', profit)


def make_report(portfolio, prices):
    '''
    Reads in portfolio and current price list
    calculates the change in pice
    returns a list of tuples with Name, Shares, Price Change
    portfolio and prices are the dics created above
    '''
    report = []
    for s in portfolio:
        line = (s['name'], s['shares'],s['price'],prices[s['name']]-s['price'])
        report.append(line)
    return report
