# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

prices = [7,1,5,3,6,4]

output = 0
#Initialize two pointers 
l,r = 0,1

#r should run until right pointer is less than length of list
while r < len(prices):
    #price at index l is less than the price at index r
    if prices[l]<prices[r]:
        #calculate the profit
        profit = prices[r]-prices[l]
        #add to output
        output = max(output,profit)
    else:
        #if not profitable then we update this pointer to r now 
        l = r
    #now we will see for any further possibilities
    r += 1

print(output)
#runs in python3 