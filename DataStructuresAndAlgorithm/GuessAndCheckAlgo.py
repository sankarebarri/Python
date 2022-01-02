def isPerfectCube(num):
    ans = 0
    while ans**3 < abs(num):
        ans += 1
    if ans**3 != abs(num):
        print("Not a perfect cube")
    else:
        if num < 0:
            ans = -ans
        print(ans, "is a cube root of", num)
def main():
    if __name__ == "__main__":
        print(isPerfectCube(8), "answer is 2")
        print(isPerfectCube(-8), "answer is -2")
        print(isPerfectCube(9), "answer is not perfect cube")
        
main()