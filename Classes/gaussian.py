import numpy as np

import math
class Gaussian:
    
    def __init__(self, mu=0, sigma=1):
        
        self.mean = mu
        self.stdev = sigma
        self.data = []
        
    def calculate_mean(self):
        
        self.mean = np.mean(self.data)
        return self.mean
    
    def calculate_stdev(self, sample=True):
        
        x_mean = self.calculate_mean()
        
        mean_item_squared = []
        for i in range(len(self.data)):
            mean_item = (self.data[i] - x_mean)**2
            mean_item_squared.append(mean_item)
         
        self.stdev = math.sqrt(np.sum(mean_item_squared) / len(self.data))
        sample_length = len(self.data)
        if sample:
            self.stdev = math.sqrt(np.sum(mean_item_squared) / (sample_length-1))
            return self.stdev
        
        return self.stdev
    
    def read_data_file(self, file_name, sample=True):
        
        
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(line)
                line = file.readline()
        file.close()
        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample=True)

    def __add__(self, other):
        results = Gaussian()
        results.mean = self.mean + other.mean
        results.stdev = math.sqrt(self.stdev**2 + other.stdev**2)
        
        return results
        
    def __repr__(self):
        return f'mean is {self.mean}, stdev is {self.stdev}'
        
    
data = [9, 2, 5, 4, 12, 7]

gaussian = Gaussian()
gaussian.data = data
print(gaussian.calculate_mean())
print(gaussian.calculate_stdev(sample=True))
gaussian_one = Gaussian(5, 2)
gaussian_two = Gaussian(7, 3)
gaussian_sum = gaussian_one + gaussian_two
print(gaussian_sum)
print(gaussian_sum.stdev)
print(gaussian_sum.mean)
            