# Input: s = "anagram", t = "nagaram"
# Output: true
# Input: s = "rat", t = "car"
# Output: false

s = "anagram"
t = "nagaram"

#strings can be sorted using join and sorted 
#sorted gives a new string and can be stored in new variable

string_1 = ''.join(sorted(s))

string_2 = ''.join(sorted(t))

#check if both the strings are same or not
if string_1 == string_2:
    print("True")
else:
    print("False")