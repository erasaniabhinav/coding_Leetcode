# Input: s = "()[]{}"
# Output: true
# Input: s = "()"
# Output: true

s = "()[]({}"
stack = []
#mapping closing to opening in a dict(hasmap)
closetoopen = {")":"(","}":"{","]":"["}

#iterating through every character
for i in s:
    #if i is in keys of closetoopen(closing)
    if i in closetoopen:
        #checking if stack is not empty and the last element equals value of i
        if stack and stack[-1] == closetoopen[i]:
            stack.pop()
        else:
            print(False)
    else:
        #if we get an open instead of close(keys)
        stack.append(i)

if len(stack) == 0:
    print(True)
else:
    print(False)
#runs in python3




