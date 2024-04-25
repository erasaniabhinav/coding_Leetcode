# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

n = 3

#initialize the first two steps 0 and 1st step
x, y = 0, 1

'''
To reach the n-th step, you can either climb from the n-1 step by taking one step,
or from the n-2 step by taking two steps.
Therefore, the total number of distinct ways to climb to the n-th step
is the sum of the number of distinct ways to reach the (n-1)-th step and the number of distinct ways to reach the (n-2)-th step.
'''

#iterate through n
for i in range(n):

    res = x + y
    #x represents distinct ways to reach the n-1 step
    x = y
    #y represents distinct ways to reach the n-2 step.
    y = res
print (res)

#   def climb(n):
#              if n==1: #only one step option is availble
#                  return 1
#              if n ==2: # two options are possible : to take two 1-stpes or to only take one 2-steps
#                  return 2
#              return climb(n-1) + climb(n-2)
#          return climb(n)