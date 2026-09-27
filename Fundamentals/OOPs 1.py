# # print("hello world")
"""class and object"""
# # class Student:
# #     name = "arsh tiwari"
# # s1 = Student()
# # print(s1.name)
# # s2 = Student()
# # print(s2.name)

# # class Car:
# #     color = "blue"
# #     brand = "scorpio"
# # Car1= Car()
# # print(Car1.color)
# # print(Car1.brand)
# class Student:
# #     #default constructor
# #     # def __init__(self):
# #     #     pass
# #     #     print("my work is doing programming ")
# #     #parameterised constructor
#     collage_name = "st.wilfred collage of computer science"
#     def __init__(self,name, mark):
#         self.name = name
#         self.mark = mark

#         print("my work is doing programming ")


# s1 = Student("arsh tiwari",98)
# print(s1.name,s1.mark,s1.collage_name)

# s2 = Student("arsh tiwari",89)
# print(s2.name,s2.mark)

# print(Student.collage_name)

# class Function:
#     def __init__(self,name,member,day,work):
#         self.name = name
#         self.member = member
#         self.day = day
#         self.work = work
#         print("enjoy yor festivel")

# f1 = Function("ankush",5,"Mondey","food")
# f2 = Function("aditya", 28,"friday","dance")
# print(f1.name, f1.member)
# print(f2.name)


""""Mathods"""
# class Student:
#     college_name ="ABC Collage"
#     def __init__(self,name, mark):
#         self.name = name
#         self.mark = mark
#     def hello(self):
#         print("welcome student",self.name)

#     def get_marks(self):
#         return self.mark


# s1 = Student("ankush",98)
# s1.hello()
# print(s1.get_marks())
"""static  method """

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     @staticmethod
#     def hello():
#         print("hello world")
#     def get_avg(self):
#         sum = 0
#         for value in  self.marks:
#             sum += value
#         print("hi",self.name,"your avg score is:",sum/3)

# s1 = Student("Ankush",[98,89,79])
# s1.get_avg()

# s1.name= "aditya"
# s1.get_avg()
# s1.hello()

"""Abstraction (Hinding the inplementation details form the user
showing only nessecery information"""

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk= False
#         self.clutch= False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started....")

# car1 = Car()
# car1.start()

"""Encapsulation(wrpping data into single unit  object)"""


# class Account:

#     def __init__(self,bal,acc):

#         self.balence = bal
#         self.account_no = acc
# # debit mathod

#     def debit(self,amount):
#         self.balence -= amount
#         print("Rs.",amount,"was debited")
#         print("total balence = ", self.get_balence())

# #credit mathod
#     def credit(self,amount):
#         self.balence += amount
#         print("Rs.",amount,"was credit")
#         print("total balence = ", self.get_balence())
    
#     def get_balence(self):
#         return self.balence

# acc1 = Account(10000,1234)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(50000)
# acc1.debit(8665)



# print("hello world")
