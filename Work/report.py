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
