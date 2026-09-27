# print("hello world")
# #string
# # we can also use single and double cotes
# str1 = "my name is arsh tiwari"
# print(str1)
# # concatenation
# str1 = "arsh"
# str2 = "tiwari"
# print(str1+str2)
# #printing the length of the string
# str1 = "arsh"
# print(len(str1))
# # Indexing(always started form the 0 its help to access the number)
# str = "my name is arsh tiwari"
# char = str[5]
# print(char)
# # slice(accessign the part of the element)
# str = "Ankush tiwari"
# print(str[1:4]) #last index can not be included
# str= "Apple"
# print(str[-5:-2])
# str = "my name is arsh tiwari"
# print(str.endswith("y"))
# str = "my name is arsh tiwari"
# print(str.capitalize())
# str = "my name is arsh tiwari"
# print(str.replace("tiwari", "tripathi"))
# print(str.find("r"))
# print(str.count("e"))
# # Questionn no 1
# # WAP input user name and count the length
# name = input("enter your name :")
# print(len(name))
# str = "my name is  mahadev mahapati"
# print(str.count("a"))



# # Conditional statement(if , else , elif )
# age = int(input("enter your name :"))
# if(age >= 18):
#     print("you are aligible for the licence")#spac is called as indentation)
# else:
#     print("you are not able for the licence")


# # question number 2(assognning grade on basic of the student mark )
# mark =int(input("enter your  marks:-"))
# if(mark >= 90):
#     print("you passed with A grade")
# elif(mark >=80 and mark < 90):
#     print('your passed with B grade')
# elif(mark >=70 and mark < 80):
#     print("your passed with the grade C")
# else:
#     print("you passed with the grade D")

# # nesting(if statement inside the if condition)
# age =int(input("enter your age:-"))
# if(age >= 18 ):
#     if(age >= 80):
#         print( " you can not be drive yet becouse your age is to more")
#     else:
#         print( " you can drive")
# else:
#     print("you can not be drive yet")
#     print("please check your  age ")

# # Question 1 = WAP to check if a number entered by the user is odd or even
# num  = int(input("enter your number:"))
# if(num % 2 == 0):
#     print("number is even")
# else:
#     print("number is odd")

# # Question 2 - WAP to find the greatest of three number enter by the user
# a = int(input("enetr your number :-"))
# b = int(input("enetr your number :-"))
# c = int(input("enetr your number :-"))
# if(a>b and a>c):
#     print("a is gartest number" , a)
# elif(b>c and b>a):
#     print(" b is the gretest number",b)
# elif(c>a and c>b):
#     print("c is the gretest number",c)
# else:
#     print("all number are the equal")

# # Question 2 - WAP to check if a number is multiple of  7 or not
# number =  int(input("enetr your number::"))
# if(number % 7 == 0):
#     print("number is multiple of the 7")
# else:
#     print("number is not multiple of the  7")