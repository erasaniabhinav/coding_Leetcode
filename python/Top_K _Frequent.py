# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Input: nums = [1], k = 1
# Output: [1]

nums = [1,1,1,2,2,3]
k = 2

#initialize an empty dictionary to store the count of nums repeated
count = {}

#iterating through nums
for i in nums:
    #if i not in keys of count then add as new key
    if i not in count:
        count[i] = 1
    #if already key exists then append an extra 1
    # Increment the value associated with the key by 1
    else:
        count[i] += 1
        
print(count)
#print(count.keys())






