def calculator():
    a = int(input("enter your first number:-"))
    b = int(input("enter your  second number:-"))
    def add(a,b):
        print("addition of these number=",a+b)
        
    def subtract(a,b):
        print("subtraction of these number=",a-b)
        
    def multiply(a,b):
        print("multiplecation of these number=",a*b)
    def division(a,b):
        if b!= 0:
            print("division  of these number= " ,a/b)
        else:
            print("invalid  number it can not be zero!!!!!")
    def square(a,b):
        print("square of these number",a**b)
    def num(a,b):
        i = a
        while a <=b:
            print(a)
            a+=1
    #choise operation
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. printing number form a to b")

    choise =int(input("enter choise(1,2,3,4 ,5,6 :-)"))

    if choise== 1:
        add(a,b)
    elif choise == 2:
        subtract(a,b)
    elif choise == 3:
        multiply(a,b)
    elif choise == 4:
        division(a,b)
    elif choise == 5:
        square(a,b)
    elif choise == 6:
        num(a,b)
    else:
        print("choise out pf range !!!")

calculator()