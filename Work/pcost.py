# pcost.py
#
# Exercise 1.27
import sys
import csv
import report

def portfolio_cost(filename):
    '''
    Calculates total cost of share portfolio
    Adusted to use csv package
    Adjusted to be able to call a fileneame from the terminal
    '''
    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

'''
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
  
print('Total cost:', cost)
'''
