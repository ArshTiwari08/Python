# mathod one
num = [1,2,4,3,2,5,2,6,3,8,4,7,2]
freq_dict = {}
for i  in range(0, len(num)):
    if( num[i] in freq_dict):
        freq_dict[num[i]] +=1 
    else:
        freq_dict[num[i]] = 1

print(freq_dict)
# print(freq_dict[2])

# Mathode - 2
num = [1,2,4,3,2,5,2,6,3,8,4,7,2]
hash_map={}
n = len(num)
for i in range(0,n):
    hash_map[num[i]] = hash_map.get(num[i],0)+1
    # hash_map[num[i]] = hash_map.get(num[i],0)+1

print(hash_map)