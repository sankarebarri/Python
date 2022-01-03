def countVowel(s):
    count = 0
    for c in s:
        c = c.lower()
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            count += 1
    return count

def main():
    if __name__ == "__main__":
        s = 'azcbobobegghakl'
        print(countVowel(s), "=5 vowels here")
main()