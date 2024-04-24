# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

nums = [0,0,1,1,1,2,2,3,3,4]

#we initialze empty array and also k
result = []
k = 0

#iterates through nums
for i in nums:
    #if number in nums not in result(empty at first)
    if i not in result:
         #add it to result
         result.append(i)

#checks for the count of unique elements 
for j in result:
     k += 1
     

print(k,result)