# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

numbers = [2,7,11,15]
target = 9
#Output should be : [1,2]

#first iteration goes from 0 to len(numbers)
# for i in range(len(numbers)):
#     #second goes from i+1 to len(numbers) to check for consecutive indices
#     for j in range(i+1,len(numbers)):
#         #if matches the target
#         if numbers[i] + numbers[j] == target:
#             #we return the indices by adding 1 to each
        
#             print(i+1,j+1)

left, right = 0, len(numbers) - 1
        
while left < right:
            
    current_sum = numbers[left] + numbers[right]
    if current_sum == target:
            print [left + 1, right + 1]
            break

    elif current_sum < target:
            
            
            # Move the left pointer to the right to increase the sum
            left += 1
    else:
            
                # Move the right pointer to the left to decrease the sum
            right -= 1

