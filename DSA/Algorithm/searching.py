# linear seaching 

nums = [2,5,2,1,6,3,7,2]
n = len(nums)
target = 6
for i in range(n):
    if nums[i] == target:
        print(i)



# binary search
nums = [2, 5, 2, 1, 6, 3, 7, 2]
nums.sort()
print(nums)
target = 6
n = len(nums)
left = 0
right = n - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(-1)