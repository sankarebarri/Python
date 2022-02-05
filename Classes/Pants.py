class Pants:
    '''
    color (string) eg 'red', 'yellow', 'orange'
    waist_size (integer) eg 8, 9, 10, 32, 33, 34
    length (integer) eg 27, 28, 29, 30, 31
    price (float) eg 9.28
    '''
    def __init__(self, color, waist_size, length, price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price
        
    def change_price(self, new_price):
        '''
        Args:
            new_price (float): the new price of the shirt
        Returns:
            None
        '''
        self.price = new_price
        
    def discount(self, discount):
        '''
        Args:
            discount (float): a decimal value for the discount. For example 0.05 for a 5% discount.

        Returns:
            float: the discounted price
        '''
        return self.price * (1-discount)
    