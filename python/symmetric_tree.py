# Input: root = [1,2,2,3,4,4,3] #check whether it is a mirror of itself (i.e., symmetric around its center).
# Output: true 
'''
     1
 2   |  2
3  4 | 4  3

'''
root = [1,2,2,3,4,4,3]

x = []
y = []

x.append(root[0])
y.append(root[0])

x.append(root[1])
y.append(root[2])

x.append(root[3])
x.append(root[4])

y.append(root[5])
y.append(root[6])


print(x)
print(y)

#PENDING