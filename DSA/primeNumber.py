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


# to print all the prime number between 0 to n
# to print all the prime number between 0 to n

def isPrimeNumber(n):
    if n <=1:
        return False
    i = 2
    while i*i <=n:
        if n%i == 0:
            return False
        i+=1
    return True

def printPrime_num(n):
    for i in range(n):
        check = isPrimeNumber(i)
        if check == True:
            print(i)
    
printPrime_num(10)
