def countBob(s):
    '''
    Counts how many times the word 'bob'
    appears in the string s
    s: string
    '''
    count = 0
    for i in range(len(s)):
        if s[i:i+3] == 'bob':
            count += 1
    return count

def main():
    if __name__ == "__main__":
        s = 'boobobobboszbobb'
        s1 = 'kobobbobwbobobboobbobbya'
        s2 = 'sdfdfcdfghbfggffgdfcgvd'
        print(countBob(s), "=3times")
        print(countBob(s1), "=5times")
        print(countBob(s2), "=0times")

main()