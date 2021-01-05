# stock.py

# Ex 4.1

class Stock:
    __slots__ = ('name','_shares','price')
    # slots makes code more memory efficent but should be avoided
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'
    '''    
    Below is is how the above is represented in the answers
    Which looks like something to do with reading it as a string
    def __repr__(self):
    return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
    '''
    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected integer')
        self._shares = value

    @property
    def cost(self):
        ''' calculate shares*price '''
        return self.shares * self.price

    def sell(self, nshares):
        ''' sell some shares, changes shares object '''
        self.shares -= nshares