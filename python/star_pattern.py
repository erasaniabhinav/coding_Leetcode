#output: *
#        * *
#        * * *

#takes in an input n
def print_star(n):
    #iterates through n
    for i in range(n):
        #iterates again
        for j in range(i+1):
            print("*",end = ' ')
        print()

print_star(7)
print_star(9)
print_star(10)