# Extraction of the Digit
# 1) Count Digit
# 2) Reverse a number
# 3) Check pelindrom
# 4) armstrong number

import math
# # Counting the digit
number  = 12424543234543
n = number
# count = 0
# while n > 0:
#     n = n//10
#     count += 1
# print()
# print("total count of that number is :-", count)

# ++++++OR++++++++
# def count_Number(number):
#     return int(math.log10(number)+1)

# print(count_Number(123457784884))

# # Reversing the number 
# number = 1234
# n = number
# while n > 0:
#     last_digit = n %10
#     print(last_digit,end="")
#     n = n//10


# # Checking the Pelindrom
# name = "nitin"
# idx = len(name)-1
# check = ""
# while idx >=0:
#     check+=name[idx]
#     idx -=1
# if(check == name):
#     print("this is an pelindromic word")
# else:
#     print("not an a pelindromic word")


# Checking the amstrong Number

# number = 1634
# n = number


# power = len(str(number))
# total = 0
# while n > 0:
#     last_digit = n %10
#     total +=  last_digit **power
#     n = n//10

# if(number == total):
#     print("this is an amstrong number ")
# else:
#     print("this is not an amstrong number")