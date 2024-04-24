#Input: strs = ["flower","flow","flight"]
#Output: "fl"

strs = ["flower","flow","flight"]
#index in list: 0,1,2

# Initialize an empty string to store the common prefix
s = ""
# Get the length of the shortest string 
l = len(min(strs, key=len))
        
# Sort the list of strings 
strs.sort()
        
# Iterate through the characters of the shortest string
for i in range(l):
# Check if the character at the current position is the same in the first and last strings
    if strs[0][i] == strs[-1][i]:

# If it's the same for all strings, append the character to the common prefix
        s += strs[0][i]
    else:
# If not, break out of the loop
        break
        
# Return the longest common prefix
print(s)


    

