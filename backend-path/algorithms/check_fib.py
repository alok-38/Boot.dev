from math import sqrt, floor

def isPerfectSquare(number):
    if number < 0:
        return False
    root = sqrt(number)
    return floor(root) * floor(root) == number

def isFeb(n):
    x = 5 * n * n + 4
    y = 5 * n * n - 4
    return isPerfectSquare(x) or isPerfectSquare(y)

print(isFeb(1))  
