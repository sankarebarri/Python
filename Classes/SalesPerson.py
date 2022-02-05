class SalesPerson:
    '''Attributes:
        first_name: str
        last_name: str
        employee_id: int
        salary: float
    
    Methods:
        sellpants() to append pants_objects to the pants_sold
        display_sales() to display the characteristics of each pants_object
        calculate_sales() to calculate the total cost of each pants
        calculate_commision() to calculate the commision of the salesperson
    '''
    def __int__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants_object):
        '''
        Appends pants_object to the pants_sold attribute

        Args:
            pants_object: pants object from the Pant class
        '''
        self.pants_sold.append(pants_object)

    def display_sales(self):
        '''
        display the characteristics of each pants_object
        '''
        for pant in self.pants_sold:
            print(f'color: {pant.color}, waist_size: {pant.waist_size}, length: {pant.length}, price:{pant.price}')

    def calculate_sales(self):
        '''
        calculate the total cost of each pants

        Returns: the sum of each pants_sold
        '''
        total_sales = 0
        for pant in self.pants_sold:
            total_sales = total_sales + pant.price
        return total_sales

    def calculate_commision(self, percentage):
        '''
        calculate the commision of the salesperson based on percentage given
        Args:
            percentage: float between 0 and 1
        '''
        total_sales = self.calculate_sales()
        return total_sales * percentage