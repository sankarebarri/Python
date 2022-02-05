class SalesPerson:
    def __int__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants_object):
        self.pants_sold.append(pants_object)

    def display_sales(self):
        for pant in self.pants_sold:
            print(f'color: {pant.color}, waist_size: {pant.waist_size}, length: {pant.length}, price:{pant.price}')

    def calculate_sales(self):
        total_sales = 0
        for pant in self.pants_sold:
            total_sales = total_sales + pant.price
        return total_sales

    def calculate_commision(self, percentage):
        total_sales = self.calculate_sales()
        return total_sales * percentage