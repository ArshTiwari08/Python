
# to find the the number of factor
import math
def checkFactor(num):
    factor = []
    i = 1
    while  i <= num:
        if(num % i ==0):
            factor.append(i)
        i+=1
    return factor

# print(checkFactor(20))

# better solution
def check_factor(num):
    factor = []
    for i in range(1,num//2+1):
        if(num % i == 0):
            factor.append(i)
    factor.append(num)
    return factor

# print(check_factor(20))


# more optimal solution
def check_factor(num):
    factor = []
    i = 1
    while i * i <= num:
        if num % i == 0:
            factor.append(i)
            if i!= num //i:
                factor.append(num//i)
        i+=1
    return (factor)

print(check_factor(36))

#using maths 
def check_factor(num):
    factor =[]
    for i in range(1,int(math.sqrt(num))+1):
        if num % i == 0:
            factor.append(i)
            if num //i != i:
                factor.append(num //i)
    return sorted(factor)
print(check_factor(36))