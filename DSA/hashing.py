# Hashing is a technique used to store data in a way that allows fast searching, insertion, and deletion
# +++++++++++OR ++++++++++
# Prestoring value into some datastructure like list/dict/set and fetch  on it 

m = [1,2,4,3,2,1,5,3,6,4,3,0,6,4,7,10]
n = [10,102,23,2,1,4,2,6,7,292]

# hash_list = [0]*11
# for num in m:
#     hash_list[num]+=1
# for num in n:
#     if(num<1 or  num >10):
#         print(0)
#     else:
#         print(hash_list[num])

hash_dict = dict()

for i in range(0,len(m)):
    hash_dict[m[i]] = hash_dict.get(m[i],0)+1
# for j in range(0,len(n)):
#     if(n[j])=