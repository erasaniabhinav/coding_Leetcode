# Input: nums = [1,2,3,1]
# Output: true
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

nums = [1,2,4,3]

#set has only inqie elements
output =  list(set(nums))

# for i in nums:
#     if i not in output:
#         output.append(i)
#     else:
#         print("False")
#         break

#check if set equals output ot not 
#we check the length of nums and output because even if the nums is not sorted

if len(nums) == len(output):
    print("True")
else:
    print("False")
