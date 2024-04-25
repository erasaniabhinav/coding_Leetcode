# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

output = []

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

#iterate through the elements in num1
for i in nums1:
    #add them to the output list
    output.append(i)

#iterate through the elements in num2
for j in nums2:
        #add them to the output list
        output.append(j)

#print(output)
#sort the output list in ascending order
output.sort()

print(output)

#create an empty list to store values with out any zeros
res = []

for i in output:
    #if values not equal to 0 then we add them to res list
    if i != 0:
         res.append(i)
          
      

print(res)