def NearestInt(n,m):
    q = int(n/m)
    n1 = m*q
    if(n*m > 0):
        n2 = m*(q+1)
    else:
        n2 = m*(q-1)
    if(n*m > 0):
        n3 = m*(q+2)
    else:
        n3 = m*(q-2)

    if(abs(n-n1) < abs(n-n2) <abs(n-n3)):
        return n1
    return n2,n1,n3
print(NearestInt(45,17))

#  for checking the consucative number are in eqaul to the sum of the number

def isSumOfConsecutive(n):
    for i in range(1,n):
        sum = 0
        for j in range(i,n):
            sum += j
            if(sum == n and j >1):
                return True
            if(sum >n):
                break
    return False

print(isSumOfConsecutive(15))

def isSumOfConsecutive(n):
    return n > 0 and (n & (n - 1)) != 0