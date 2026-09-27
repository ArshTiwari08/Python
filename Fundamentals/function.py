# print("hello world")
# ## block of statement to perform the specific task
# # function used to reduce the redendency  in the code
# def sum(a,b):#(def is the function defination )
#     print(a+b)
#     return
# sum(5,2)
# sum(9,8)
# sum(9,156)

# ##to calculate the avrage of three number

# def avg(a,b,c):
#     avg = ((a+b+c)/3)
#     print(avg)
#     return
# avg(12,52,63)
# avg(16,18,20)

# #TYPE OF FUNCTION
# # BUILD IN FUNCTION(ALREDY BUILD BY PYTHON)
# # USER DEFINED FUNCTION(DEFINED BY THE USER)

# #to calculate the  product of the number
# def product(a= int(input("enter your number")),b = int(input("enter your number"))):
#     print(a*b)
#     return
# product()

# #question number 1 -=== print the number in the single line
# result= [ 4,5,2,5,6,3,5,6,3,5]
# def print_len(result):
#     for  item in result:
#         print(item, end="  ")
# print_len(result)

# #question number `2` -=== print the length of the list (list id the parameter)

# list = ["Ankush", "aditya", "rahul", "aman"]
# def print_len():
#     print(len(list))
# print_len()

# # printing factorial using function

# n = int(input("enter your number"))
# def calc_fact(n):
#     i = 1
#     factorial = 1
#     while i <= n:
#         factorial *= i
#         i += 1
#     print(factorial)

# calc_fact(n)

# #Question number 4 WAF to convert USD to INR

# def convertor(usd_val):
#     inr_val=usd_val*83
#     print(usd_val, "USD =",inr_val,"INR")

# convertor(10)

# #question
# a = int(input("enter your number :- "))
# def check():
#     if(a % 2==0):
#         print("number is even")
#     else:
#         print("number is odd")
# check()




# #RECURSION( when a fuction call itself repeatedlly)
# def show(n):
#     if(n == 0):#(base case)
#         return
#     print(n)
#     show(n-1)

# # show(10)

# def num(i, n):
#     if i > n:
#         return
#     print(i)
#     num(i + 1, n)

# num(1, 10)
# def show(n):
#     if(n == 0):#(base case) importent
#         return
#     print(n)
#     show(n-1)
#     print("END")
# show(3)


# #REOCCRENCE RELATIONSHIP(n! = (n-1)! * n)

# def fact(n):
#     if (n == 1 or n==0):
#         return 1
#     return fact(n-1)*n

# print(fact(5))

# #question number 1  to calculate the sum of n netural number.
# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1) + n
# sum =calc_sum(5)
# print(sum)

# # question number 2 prijnting all elenment in the list
# def print_list(list,idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# fruits = ["apple","mango","banana","payaya"]
# print_list(fruits)
