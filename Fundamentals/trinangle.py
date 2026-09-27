# print("hello world")
# #  code for printing the number in the triangle form

n = int(input("enter your number:-"))
for i in range(n+1):
    for j in range(i):
        print("*",end=(""))
    print()



# # if you want to go back from the same step to first use  for the same code 
# n = int(input("enter your number:"))
# for i in range( 1, n+1):
#     for j in  range(i):
#         print(i , end="")
#     print()
# for i in range(n-1,0,-1) :
#     for j in  range(i):
#         print(i , end="")
#     print()


# #to printing the number in the same but but i will completely reverse to the second one;
# n = int(input("enter your number :- "))
# for i in range (n,0, -1):
#     for j in range(i):
#         print(i, end ="")
#     print()
# for i in range (1,n+1):
#     for j in range(i):
#         print( i,end = "")
#     print()

# ### for printing the number 5 to 1

# n = int(input("enter your number :- "))
# for i  in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# ### for printing the number 1 to 5
# n = 5
# for i  in range(1, n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# ### for printing the number 5 x 5
# n = int(input("enter your number"))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

# ### for printing the border of right angle triangle

# n = int(input("enter your value :-"))
# for i in range(1,n+1):
#     if i == n:
#         for j in range(n):
#             print("*",end=" ")
#     else:
#         for j in range(i):
#             if j ==0 or j==i-1:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#     print()

# ####  for printing the number in lower order

# n = int(input("enter your number:"))
# for i in range(n,0,-1):
#     for j in  range(1,i+1):
#         print(j,end=" ")
#     print()

# #####reverse piramid shape 

# n = int(input("enter your number")) # number of rows
# for i in range(n):
#     for j in range(i):       # print spaces
#         print(" ", end=" ")
#     for k in range(2*(n-i)-1):  # print stars
#         print("*", end=" ")
#     print()  # move to next line

# n = 5  # number of rows
# for i in range(n,0,-1):
#     # print spaces + stars in one line
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))




# ###right piramide of the number

# n = int(input("enter your number")) # number of rows
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()

# n = 5  # number of rows
# for i in range(n):
#     # print spaces + stars in one line
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))

####3 to printing the numberin diamond form 

# class Solution:
#     def printDiamond(self, N):
#         for i in range(1, N + 1):
#             print(" " * (N - i) + "* " * i)

#         for i in range(N, 0, -1):
#             print(" " * (N - i) + "* " * i)
