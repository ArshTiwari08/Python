# to remove the all the duplicate 
# arr = [2, 4, 3, 2, 5, 1, 4, 6, 3, 2, 7, 5]
# # arr should be sorted before appling the two pointer approch
# arr.sort()

# i = 0
# j = 1
# n = len(arr)

# while j<n:
#     if arr[i]!= arr[j]:
#         i+=1
#         arr[i] = arr[j]
#     j+=1

# print(arr[:i+1])


# Using the two pointer from the opposite site

# Q- Add two number  to get the target

nums = [5,2,6,3,2,7,2,7,2]
target = 10
nums.sort()
print(nums)

n = len(nums)
left = 0
right = n-1
while left<right:
    total = nums[left]+nums[right]
    if total == target:
        print(nums[left],nums[right])
        left +=1
        right -=1
    elif total < target:
        left+=1
    else:
        right -=1
