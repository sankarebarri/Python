def reverseList(array):
    '''
    It returns the reverse of a given list
    Parameters: The array is a list
    '''
    accumulator = []
    for x in array:
        accumulator = [x] + accumulator
    return accumulator

def main():
    if __name__=="__main__":
        L = [1,2,3,4,5]
        L1 = ['a','b','c','d','e']
        print(reverseList(L))
        print(reverseList(L1))

main()