# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

nums = [-1,0,1,2,-1,-4]

output = []
#a+b+c = 0
#sort the input array 
nums.sort()
#iterate through index and value
for i, a in enumerate(nums):
    #not using the same value again, if equals before number: continue
    #current value a is the same as the previous value nums[i-1] 
    #and also different from the value before it nums[i-2]
    if i > 0 and a == nums[i-1] and a != nums[i-2]:
        continue 
     
    l,r = i+1,len(nums)-1
    #left and right cant be equal: this is like two sum solution from here
    while l<r:
        threesum = a + nums[l] + nums[r]
        if threesum > 0:
            r -= 1
        elif threesum < 0:
            l += 1
        else:
            output.append([a,nums[i],nums[r]])
            #update left pointer
            l += 1
            #if its the same value we shift the value again 
            #left pointer should not pass right
            while l < r and nums[l] == nums [l-1]:
                l += 1

print(output)
#runs in python3 






 
