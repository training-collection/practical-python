# stock.py

# Ex 4.1

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        ''' calculate shares*price '''
        return self.shares * self.price

    def sell(self, nshares):
        ''' sell some shares, changes shares object '''
        self.shares -= nshares