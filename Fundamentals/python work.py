n = int(input("enter your number:"))
for i in range(1,n+1):
    if i == n:
        for j in range(n):
            print("*",end=" ")
    else:
        for j in range(i):
            if j==0 or j==i-1:
                print("*", end=" ")
            else:
                print(" ",end=" ")
    print()