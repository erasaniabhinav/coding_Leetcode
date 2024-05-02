# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

tokens = ["2","1","+","3","*"]

x = []

#iterates through every element in tokens
for i in tokens:
    #if an element is digit then adds its int value to x
    if i.isdigit():
        x.append(int(i))
    #If the token is an operator (+, -, *, /)
    else:
        #we take the last 2 elements out and check for i
        element2 = x.pop()
        element1 = x.pop()

        if i == '+':
            x.append(element1+element2)
        elif i == '-':
            x.append(element1-element2)
        elif i == '*':
            x.append(element1*element2)
        elif i == '/':
            x.append(element1/element2)
        
print(x)

