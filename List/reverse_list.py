def reverseList(array):
    '''
    It returns the reverse of a given list
    Parameters: The array is a list
    '''
    accumulator = []
    for x in array:
        accumulator = [x] + accumulator