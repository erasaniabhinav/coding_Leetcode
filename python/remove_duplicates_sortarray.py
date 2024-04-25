# Input: head = [1,1,2]
# Output: [1,2]
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

head = [1,1,2,3,3]
output = []

#iterate through the array given
for i in ((head)):
#    print(i)
    #checks for values at every index and if not duplicated
    if i not in output:
         #adds to the output list
         output.append(i)


print(output)


