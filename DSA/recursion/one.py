# def eat_mangoes(count):
#     if count == 0:
#         print("hand is empty . done")
#         return
    
#     print(f"i have {count} mangoes in my hand.end one")
#     eat_mangoes(count-1)

# print(eat_mangoes(5))


# def factorail(n):
#     if n == 0:
#         return 1
#     print(f"now your count become {n}")
#     return n*factorail(n-1)

# total = factorail(5)
# print(total)

# to print the fibbonacci number

n = 10
a = 1
b = 1
for i in range(n):
    print(a)
    a,b = b,a+b


# 
def fib(n):
    if n == 1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(10))