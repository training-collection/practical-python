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

# take list of stocks with origional prices in 'portfolio'
# inital_value  calculate the inital value of the portfoio with the 'price' there
# current_value calculate the new value of the portfolio with the read_prices dict
# dif calculate the gain/los

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
