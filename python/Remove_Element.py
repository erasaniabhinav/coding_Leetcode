# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

nums = [3,2,2,3]
val = 3

#initialize an empty list
result_nums = []
#initialize k = 0, k counts the result nums
k = 0


for i in nums:
    print(i)
    #while checking every index and if value at index not equal to Val
    if i != val:
        #we append the value to result 
        result_nums.append(i)


#counting the numbers in result by counter k
for j in result_nums:
    k += 1

print(k, result_nums)