# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

nums = [0,3,7,2,5,8,4,6,0,1]
#initialize output to 0
output = [0]
#sort the array ascending
nums.sort()

#[1, 2, 3, 4, 100, 200]
#iterate through nums

for i in nums:
    if i not in output and i == output[-1] + 1:
        output.append(i)


print(output)
print(len(output))


