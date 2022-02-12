class Statx:
    
    def __init__(self):
        self.data = []
        pass

    def read_data(self):
        pass
    
    def data_mean(self):
        '''
        Calculate the mean of:
            the sample_data if sample=True
            the population if sample =False
            
        Args:
            sample: boolean
        Return: The mean of the data
        '''
        len_data = len(self.data)
        if sample:
            len_data = len_data - 1
            return sum(self.data)/len_data
        return sum(self.data)/len_data

    def data_median(self):
        '''
        Gives the median of the data
        '''
        self.data.sort()
        length = len(self.data)
        if length%2 !=0:
            return self.data[length//2]
        return((self.data[length//2] + (self.data[length//2] - 1)) / 2)
    
    def data_variance(self):
        pass
    
    def data_stdev(self):
        pass
    
    def data_covariance(self):
        pass
    
    def z_score(self):
        pass
    
    def skewed(self):
        '''Tells if a data is skewed
        Returns:
            Boolean: False if not skewed
            If Skewed:
                Return Skewed direction
        '''
        pass
    
    def is_sampling_normal(self):
        '''
        Tells if a sampling distribution is normal according to some given rules
        '''
        pass
    
    def sample_mean(self):
        pass
    
    def sample_proportion(self):
        pass
    
    def standard_error_mean(self):
        pass
    
    def confidence_interval(self):
        pass