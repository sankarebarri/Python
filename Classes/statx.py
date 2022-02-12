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
        if len_data == 0:
            return 0
        if len_data == 1:
            return sum(self.data)
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
        if length == 0:
            return 0
        if length%2 !=0:
            return self.data[length//2]
        return((self.data[length//2] + (self.data[length//2] - 1)) / 2)

    def data_mode(self):
        '''
        Gives the mode of the data
        Unimodal: If there is only one mode
        Mutlimodal: If there is at least 2 modes
        
        Return:
            
        '''
        if len(self.data) == 0:
            return 0
        if len(self.data) == 1:
            return self.data[0]
        count_mode = {}
        for i in range(max(self.data)+1):
            count_mode[i] = self.data.count(i)
        max_value = max(count_mode.values())
        modes = []
        for key, value in count_mode.items():
            if value == max_value:
                modes.append(key)
        if len(modes) == 1:
            return f'Unimodal data {modes[0]} occurs {max_value} times'
        return f'Multimodal data {modes} each occurs {max_value} times'
    
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