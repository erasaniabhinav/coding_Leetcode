# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Input: nums = [1,3,5,6], target = 2
# Output: 1

nums = [1,3,5,6]
target = 5

output = 0

#iterating through nums
for i in range(len(nums)):
    #if value at index equal to target
    if nums[i] == target:
        #output is index position
        output = i
        break
    else:
        #if value @i less than target and 
        if nums[i] < target:
            #value @i+1 greater than target
            if nums[i+1] > target:
                #insert the target between i+1
                output = (i+1)

            

print(output)