
def power(n,m):
#     pow = 1
#     for i in range(abs(m)):
#         pow = pow*n
#     return  pow
# print(power(3,5))

    if m ==0:
        return 1
    if m <0:
        return 1/power(n,-m)
    return n * power(n,m-1)

print(power(3,5))