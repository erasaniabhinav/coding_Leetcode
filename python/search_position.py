# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Input: nums = [1,3,5,6], target = 2
# Output: 1

nums = [1,3,5,6]
target = 5

output = 0

for i in range(len(nums)):
    if nums[i] == target:
        output = i
        break
    else:
        if nums[i] < target:
            if nums[i+1] > target:
                output = (i+1)

            

print(output)