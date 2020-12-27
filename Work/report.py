# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''Reads portfolio as tuple'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holiding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holiding)
    return portfolio
