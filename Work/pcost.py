# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    'Calculates total cost of share portfolio'
    total_cost = 0.0
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            try:
                total_cost = total_cost + float(row[1]) * float(row[2])
            except ValueError:
                print("Could not parse", line)
    return total_cost


cost = portfolio_cost('Data/missing.csv')  
print(cost)
