
def factorial(n):
    if n < 0:
        return "The factorial of negative numbers is not calculated"
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
if __name__ == '__main__':
    n = -3
    result = factorial(n)
    print(result)