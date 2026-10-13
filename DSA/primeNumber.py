def isPrimeNumber(n):
    if n<=1 :
        return False
    for i in range(2,n-1):
        if n%i == 0:
            return False
    return True

# Square root technique
def isPrimeNumber(n):
    if n <=1:
        return False
    i = 2
    while i*i <=n:
        if n%i == 0:
            return False
        i+=1
    return True
print(isPrimeNumber(5))