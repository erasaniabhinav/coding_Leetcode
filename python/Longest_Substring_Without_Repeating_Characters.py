# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

s = "abcabcbb"
#we create a set to eliminate any duplicate letters 
outputset = set()
res = 0

l = 0
#r iterates through every letter in s
for r in range(len(s)):
    #if a value is alreeady in outputset
    while s[r] in outputset:
        #we delete the first letter on the left and slide the window to right
        outputset.remove(s[l])
        #now we increment the value by 1 to right
        l += 1
    outputset.add(s[r])
    #update result, if current window is greater we find the diff r-l (index stars from 0, so)
    res = max(res,r-l+1)

print(res)
#runs in python 3



 