# to find the missing number from 0 to n
arr = [1,2,4,3,6]
n = max(arr)
# calculating the sum of the all the number from 0 to n
expected = int(n*(n+1)/2)
actual = 0
# tp calculating the sum of number prasent in the arrey
for i in arr:
    actual += i
if expected == actual:
    print("no any missing number")
missing_number = expected - actual
print("the missing number is ",missing_number)