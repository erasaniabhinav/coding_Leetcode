# Input: nums = [2,7,11,15], target = 9
#                0,1, 2, 3
# Output: [0,1]

nums = [0,21,2,5,14,7,11,15]
target = 9

#first iteration goes through the len of nums
for i in range(len(nums)):
##second iteration goes through the i+1 to len of nums
    for j in range(i+1,len(nums)):
#checks if sum matches target 
        if nums[i]+nums[j] == target:
            #we print the index positions 
            print(i,j)






