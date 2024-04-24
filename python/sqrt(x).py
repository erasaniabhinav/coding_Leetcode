# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

x = 4

left=0
right=x

while left <=right:
    mid=(left+right)//2
    if (mid*mid)==x:
        print (mid)
        break
    elif (mid*mid)<x:
            
        left=mid+1
        break
    else:
        right=mid-1
        break

print (right)
