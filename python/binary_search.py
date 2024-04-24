# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# target = 2
# Output: -1

nums = [-1,0,3,5,9,12]
target = 4

#iterating through the len of nums
for i in range(len(nums)):
    #if target is at any index in num
    if nums[i] == target:
        #we print the position index
        print(i)
        #and we break from the program as we dont want to print -1
        break

#print -1 if we dont find the target in num
else:
    print(-1)      
    
  
