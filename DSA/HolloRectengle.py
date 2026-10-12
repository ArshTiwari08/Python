def hollorectangle(n,m):
    i = 1
    while i<=n:
        j =1
        while j<=m:
            if i ==1 or i==n or j ==1 or j==m:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        print()
        i+=1
hollorectangle(4,6)

print("   Option   ")

def p(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(i ==1 or i ==n) or (j ==1 or j == m):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
p(4,6)