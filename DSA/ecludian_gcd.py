def get_gcd(a,b):

    while b != 0:
        a,b = b,a%b

    print("GCD :-",a)


def getLCD(a,b):
    product = a*b
    gcd = 0
    while b != 0:
        a,b = b,a%b
    gcd = a

    return product / gcd

result = getLCD(18,12)
print(result)