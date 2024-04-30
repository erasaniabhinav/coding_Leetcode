# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Initialize pointers 
left = 0
right = len(height) - 1
    
max_area = 0
    
while left < right:

    #width of the container
    width = right - left
        
    #height of the container (minimum height of the two)
    container_height = min(height[left], height[right])
        
    #area of the container
    area = width * container_height
        
    #maximum area if the current area is greater
    max_area = max(max_area, area)
        
    #move the pointer 
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(max_area)