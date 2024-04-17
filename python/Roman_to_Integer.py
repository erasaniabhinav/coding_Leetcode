# # Input: s = "III"
# # Output: 3
# # Explanation: III = 3

#this is the s input
s = "XIX"
#created a dict using the keys and values
d = {"I":1,"V":5,'X':10,'L':50,'C':100,'D':500,'M':1000}

total_sum = 0

#iterating through the entire len of s
for i in range(len(s)-1):
    #checks if s is in d.keys
    if s[i] in d:
        if s[i+1] == "X" or s[i+1] == "V":
            total_sum = total_sum - 1
        else:

            total_sum += d[s[i]]
        

print("total_sum:",total_sum)
        

