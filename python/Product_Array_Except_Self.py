# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


nums = [1,2,3,4] 

#initialize the product and output list 

product = 1
output = []

#find the total product of the elements of list 
for i in nums:
    product = product * i

#print(product)

#divide by number itself at every index

for j in nums:
    #dividing the product by every number 
    x = product//j
    #adding it to the output list
    output.append(x)

print(output)