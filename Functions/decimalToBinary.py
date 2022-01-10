def decimalToBinary(num):
    '''Takes in a decimal digit and convert it to binary digits'''
    if num < 0:
            isNegative = True
            num = abs(num)
    else:
        isNegative =  False
    bin_num = ''
    while num != 0:
        r = num % 2
        num = num // 2
        bin_num = str(r) + bin_num
    if isNegative:
        bin_num = '-'+bin_num
    return bin_num

def decimalFractionToDecimal(num):
    pass