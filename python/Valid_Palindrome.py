# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

s = "A man, a plan, a canal: Panama"
# = "race a car"

#removes spaces and punctz from string
s_new = s.replace(" ","").replace(",","").replace(":","")
#print(s_new)
#makes string to lower case and stores its value in x
x = s_new.lower()

#print(x)
#checks if the string x is equal to its reversed value 
if x == x[::-1]:
    print(True)
else:
    print(False)
