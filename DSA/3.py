# Extraction of the Digit 
# 1) Count Digit 
# 2) Reverse a number
# 3) Check pelindrom
# 4) armstrong number


n = 1234
num = n
while num >0:
    last_digit = num % 10
    print(last_digit,end=" ")
    num = num//10

print(n)