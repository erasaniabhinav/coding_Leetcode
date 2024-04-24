# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Input: s = "luffy is still joyboy"
# Output: 6

s = "luffy is still joyboy"
output = 0


#convert the string in to list
a = [s]
#split the list using space
a = (s.split(" "))

print(a)

#iterating through the length last element
for i in range(len(a[-1])):
    #we add 1 for every letter found
    output += 1

print(output)