# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4]

digits = [1,2,3]



num = 0
for i in digits:
        num = num * 10 + i
    
    # Increment the integer by one
num += 1
    
    # Convert the incremented integer back to a list of digits
result = []
while num > 0:
    #calculates the remainder
    i = num % 10
    # inserts the rightmost digit (i) at the beginning of the result list
    result.insert(0,i)
    #updates the value of num
    num //= 10
    
print (result)
