# Input: x = 9
# Output: 3
# Explanation: The square root of 4 is 2, so we return 2.

x = 9

# Loop over each number from 0 to x-1
for i in range(x):
    # Check if the square of the current number is equal to x
    if i*i == x:
        print(i)
        # Break out of the loop
        break