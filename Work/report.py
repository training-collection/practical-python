# report.py
#
# Exercise 2.4

import csv

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

# reads the file in as a dictionary
def read_portfolio(filename):
    '''reads file as a dictionary'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        dict = {}
        for row in rows:
            dict = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(dict)
    return portfolio

# read in csv (string, float) as a dictionary
# handle blank lines

def read_prices(filename):
    '''reads file in as dictionary and handles NAN'''
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # note that there is no header

        dict = {}
        for row in rows:
            try:
                dict[row[0]] =  float(row[1])
            except IndexError:
                print("Could not parse", row)
    return dict

# 
# Calculate the gain/loss (ex 2.7)
#
'''
portfolio = read_portfolio('Data/portfolio.csv')

inital_value = 0.0
for s in portfolio:
    inital_value += s['shares']*s['price']

current_prices = read_prices('Data/prices.csv')

final_value = 0.0
for s in portfolio:
    final_value += s['shares']*current_prices[s['name']]

profit = final_value - inital_value

print('Inital value =', inital_value)
print('Final value =', final_value)
print('Profit/loss =', profit)
'''

#
# Ex 2.9 - collect data for the table
#

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
