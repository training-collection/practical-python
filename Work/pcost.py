# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(filename):
    '''
    Calculates total cost of share portfolio
    Adusted to use csv package (ex 1.32)
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


cost = portfolio_cost('Data/missing.csv')  
print(cost)
