# set and dictionary used hash table behind to save the data

# name = {} # format to create an dictinary
# work = set() # way to create an set

# frequency count


# nums = [10, 20, 30, 10, 40, 20, 50, 30, 10, 60, 20, 70, 40, 80, 30]

# def count(nums):
#     freq ={}
#     for num in nums:
#         if num in freq:
#             freq[num] = freq[num]+1
#         else:
#             freq[num]= 1
#     return freq

# print(count(nums))


signup = [
    "ankush@gmail.com",
    "ravi@gmail.com",
    "simi@gmail.com",
    "ravi@gmail.com",
    "amit@gmail.com",
    "mahesh@gmail.com",
    "ravi@gmail.com",
]

def remove_def(signup):
    seen = set()
    unique = []

    for emial in signup:
        if emial not in seen:
            unique.append(emial)
            seen.add(emial)
    return unique

print(remove_def(signup))