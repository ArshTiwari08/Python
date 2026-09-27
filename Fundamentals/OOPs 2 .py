# # print("hellow world")
# # class Student:
# #     def __init__(self,name):
# #         self.name = name

# # s1 = Student("ankush")
# # print(s1.name)

"""private Attribute"""

# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 =Account("12345","abcd")

# print(acc1.acc_no)
# print(acc1.reset_pass())

# class Person:
#     __name = "ankush"

#     def __hero(self):
#         print("hello person")

#     def welcome(self):
#         self.__hero()

# p1= Person()
# print(p1.welcome())

"""Inheritence(single)"""

# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stor():
#         print("car stopped..")
    
# class Toyotacar(Car):
#     def __init__(self ,name):
#         self.name= name
# car1 = Toyotacar("fortuner")
# car2 =  Toyotacar("prius")

# print(car1.start())
# print(car1.color)

"""inheritence (multilevel)"""

# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stor():
#         print("car stopped..")
    
# class Toyotacar(Car):
#     def __init__(self ,brand):
#         self.brand= brand

# class Fortuner(Toyotacar):
#     def __init__(self,type):
#         self.type = type

# car1 = Fortuner("deisal")
# car1.start()
# print(car1.start())
"""inheritence (multiple )"""

# class A:
#     varA= "welcome to class A"
# class B:
#     varB= "welcome to class B"
# class C(A,B):
#     varC= "welcome to class C"
# c1= C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

"""Super method"""

# class Car:
#     def __init__(self ,type):
#         self.type = type


#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stor():
#         print("car stopped..")
    
# class Toyotacar(Car):
#     def __init__(self ,name,type):
#         super().__init__(type)
#         self.name= name
#         super().start()

# car1 = Toyotacar("prius","electric")
# print(car1.type)

"""class method"""

# class Person:
#     name = "aditya"

#     # def changename(self,name):
#     #     self.__class__.name = "Rahul"

#     @classmethod
#     def changename(cls,name):
#         cls.name= name

# p1=  Person()
# p1.changename("rahul kumar")
# print(p1.name)
# print(Person.name)

"""Property"""

# class Student:
#     def __init__(self,phy,chem,math,):
#         self.phy = phy
#         self.chem = chem
#         self.maths = math
        

#     @property
#     def percentage(self):
#         return str((self.phy+ self.chem+ self.maths)/3)+ "%"

# student1 = Student(90,89,98)
# print(student1.percentage)

# student1.phy = 78
# print(student1.phy)
# print(student1.percentage)

"""polymorphism (operator overloding)"""
"""implicit overloding """

# print(1+2)
# print(type(1))

# print("arsh "+ "tiwari")
# print(type("arsh"))

# print([1,2,4]+[4,5,6])
# print(type([1,2,3]))

# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def shownumber(self):
#         print(self.real,"i+",self.img,"j")
    
#     def __add__(self,num2):#addintion for the dunder function
#         newReal = self.real +num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(1,3)
# num1.shownumber()

# num2 = Complex(4,8)
# num2.shownumber()

# num3 = num1+num2
# num3.shownumber()

"""substraction"""
# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def shownumber(self):
#         print(self.real,"i+",self.img,"j")
    
#     def __sub__(self,num2):#addintion for the dunder function
#         newReal = self.real -num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(1,3)
# num1.shownumber()

# num2 = Complex(4,8)
# num2.shownumber()

# num3 = num1-num2
# num3.shownumber()

"""question number 1"""

# class Circle:
#     def __init__(self, redius):
#         self.redius = redius

#     def area(self):
#         area =22/7 *self.redius**2
#         print(area)

#     def perimeter(self):
#         perimeter = 2*(22/7)*self.redius
#         print(perimeter)

# c1 = Circle(21)
# c1.area()
# c1.perimeter()

"""question number 2"""

# class Employee:
#     def __init__(self,role,dept,selary):
#         self.role = role
#         self.dept = dept
#         self.selary = selary

#     def showdetails(self):
#         print("role = ", self.role)
#         print("dept = ", self.dept)
#         print("selary = ",self.selary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age= age
#         super().__init__("engineer","IT", "75000")

# eng1 = Engineer("ankush", 20)
# eng1.showdetails()

"""Question number 3"""

# class Order:
#     def __init__(self,item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self,odr2):
#         return self.price > odr2.price

# order1 = Order("chips", 20)
# odr2 = Order("tea", 18)

# print(order1 > odr2)


# print("hello world")
# print("my name is ankush tiwari")
