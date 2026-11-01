# Learning Array in the python
# from array import *

# val = array('i',[1,2,3,4,5,6])
# val.insert(2,99)

# copyArray = array(val.typecode,(x*2 for x in val))

# copyArray.remove(10)
# for i in range(0,len(copyArray)):
#     print(copyArray[i],end=" ")

# a = array('i',[1,2,3,4,6,7,9,6])
# abc = a[::-1]
# for i in range(0,len(abc)):
#     print(abc[i],end=",")


# arr = array('i',[12,2,32,1,3,5,7,65,43,2,3])

# i = arr.index(65)
# print(i)

from numpy import *
# provide the hetrogeneous creation of the array
# a = array([1,2,4,5.9,6,"a"])
# a = linspace(0,100,5)
# for i in a:
#     print(i,end=",")

# a = full(10,5)
# for i in a:
#     print(i,end=",")

# a = arange(0,100,5)
# for i in a:
#     print(i,end=",")


# multidaimension array

a = [
    [1,34,5],
    [1,32,4],
    [2,43,5]
    ]
print(a[0][0])
for row in a:
    for element in row:
        print(element, end=" ")
    print()
print("Rows:", len(a))
print("Columns:", len(a[0]))

