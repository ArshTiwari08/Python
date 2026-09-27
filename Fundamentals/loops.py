print("hello world")
# loops in used to repeat the instruction

# # #while loop
# while True:
#     print("hello ")#infinite loop

# #printing the number form 1 to 5 with hello world
# i = 1
# while i <= 5:
#     print("hello world " , i)
#     i += 1

# #printing the number form 5 to 1 with hello world
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# #question number 1 (print number from 1 to 100)
# i = 1
# while i <= 100 :
#     print(i)
#     i += 1

# #question number 2 (print number from 100 to 1)
# i = 100
# while i >= 1 :
#     print(i)
#     i -= 1

# #question number 3 (print the multiplecatiion table for the number)

# n = int(input("enter your numberm :-"))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1


# #question 4(printing the number using the loop)(treversing the number)

# num = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx += 1

# # #question number 5 (serching the number using the loop)
# num = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("enter your number :-"))
# i = 0
# while i < len(num):
#     if(num[i]) == x:
#         print("found at index", i)
#     i+= 1


# #break
# i = 0
# while i <= 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1
# print()

# #question number 5 (serching the number using the loop)
# num = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("enter your number :-"))
# i = 0
# while i < len(num):
#     if(num[i]) == x:
#         print("found at index", i)
#         break
#     i+= 1


# #continue
# i = 0
# while i <= 5:
#     if i == 3:
#         i += 1
#         continue# skip
#     print(i)
#     i += 1

# # FOR LOOPS used for the sequential trevarsal in list, tuple, string  etc.


# str = "ankush tiwari"
# for char in str:
#     if char == "i":
#         print("i founded")
#         break
#     print(char)
# print("loop end")

# num = [1,4,9,16,25,36,49,64,81,100]
# for i in num:
#     print(i)

# #  question

# num = (1,4,9,16,25,36,49,64,81,100 ,36)
# x = int(input("enter your number :-"))
# idx = 1

# for  el in num:
#     if el == x:
#         print("found at index", idx)
#         break
#     idx += 1


# #RANGE(start ?, stop, step) function of range
# for i in range(10):
#     print(i)

# for i in range(2,100,2):
#     print(i)

# for i in range(101):
#     print(i)

# for i in range(100,1,-1):
#     print(i)

# n = int(input("enter your number"))
# for i in range(1,11 ):
#     print(n*i)

# ##pass statement
# for i in range(5):
#     pass
# print("some useful work")

# #Question number 1(sum of n number) using while loop
# n = int(input("enter your number:-"))
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 1
# print("total sum of the number ",sum)

# ##Question ( calculate the factorial of the number)(using while loop )
# n = int(input("enter your number:-"))
# i = 1
# fact = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("total factorial  of the number ",fact)

# ##Question ( calculate the factorial of the number)(using for  loop )
# n = int(input("enter your number:-"))
# fact = 1
# for i in range(n):
#     fact *= n
#     n-=1
# print("total factorial  of the number ",fact)

