def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact
def countZero(n):
    fact = factorial(n)
    count = 0
    while fact % 10 == 0:
        count +=1
        fact //=10
    return count

n = 6
print(countZero(n))

def trailingZeroes(n):
    
    # Edge Case
    if (n < 0):
        return -1

    # Initialize result
    count = 0

    # Keep dividing n by
    # 5 & update Count
    while (n >= 5):
        n //= 5
        count += n

    return count
trailingZeroes(6)