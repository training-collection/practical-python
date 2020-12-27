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
        for row in rows:
            #row = line.split(',')
            try:
                total_cost = total_cost + float(row[1]) * float(row[2])
            except ValueError:
                print("Could not parse", row)
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
  
print('Total cost:', cost)
