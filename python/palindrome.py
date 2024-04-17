# # Input: x = 121
# # Output: true
# # Explanation: 121 reads as 121 from left to right and from right to left.

x = 1215
#takes in x value and changes it to string
y = str(x) 

if y == y[::-1]:
#using string slicing// we check for reversed string  
    print("True")
else:
     print("False")

 

