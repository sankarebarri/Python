def bisection_squareRoot(x):
    ##numGuesses = 0
    low, high = 0.0, x
    ans = (high+low)/2.0
    epsilon = 0.01
    while abs(ans**2 - x) >= epsilon:
        if (ans**2) < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0
        #numGuesses  += 1
    return ans