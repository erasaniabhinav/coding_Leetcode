# # Input: s = "III"
# # Output: 3
# # Explanation: III = 3

#this is the s input
s = "MCMXCIV"
#created a dict using the keys and values
d = {"I":1,"V":5,'X':10,'L':50,'C':100,'D':500,'M':1000}

total_sum = 0

#iterating through len of s -1, to accomodate i+1
for i in range(len(s)-1):
    #if element in s is in d, and value of it in d < one next to it in s
    if d[s[i]] < d[s[i+1]]:
        #we minus it
        total_sum = total_sum - d[s[i]]
    else:
        #we add it to total
        total_sum += d[s[i]]
    
print(total_sum + d[s[-1]])





