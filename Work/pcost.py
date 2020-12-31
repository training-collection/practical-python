# pcost.py

import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

'''
import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')
'''
#cost = portfolio_cost(filename)
#print('Total cost:', cost)

# main function
def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfile' % args[0])
    filename = args[1]
    print('Total cost',portfolio_cost(filename))