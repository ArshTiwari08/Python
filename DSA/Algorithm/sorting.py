# # bubble sort

# def buble_sort(prices):
#     n = len(prices)

#     for i in range(n):
#         for j in range(0,n-i-1,1):
#             if prices[j] > prices[j+1]:
#                 prices[j],prices[j+1] = prices[j+1],prices[j]
#     return prices

# prices = [850,200,520,100,430]
# print(buble_sort(prices))

# #Selection sort

# def selection_sort(prices):
#     n = len(prices)

#     for i in range(n):
#         min_index = i #assuming the min_index
#         for j in range(i+1,n):
#             if prices[j] < prices[min_index]:
#                 min_index = j
#         prices[i],prices[min_index] = prices[min_index],prices[i]
#     return prices

# prices = [850,200,520,100,430]
# print("Selection sort:",selection_sort(prices))


##insertion sort

arr = [7,3,5,2]
for i in range(1,len(arr)):
    current = arr[i]
    j = i-1
    while j >= 0 and arr[j] > current:
        arr[j+1] = arr[j]
        j -=1
    arr[j+1] = current

print(arr)