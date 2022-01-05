
def consecutiveAlphabet(s):
    '''
    '''
    longest = s[0]
    current = s[0]
    for c in s[1:]:
        if c >= current[-1]:
            current += c
            if len(current) > len(longest):
                longest = current
        else:
            current = c
    return longest


def main():
    s = 'azcbobobegghakl'
    s1 = 'ndgcfgfhabcdefg'
    print(consecutiveAlphabet(s),'beggh')
    print(consecutiveAlphabet(s1),'abcdefg')

main()