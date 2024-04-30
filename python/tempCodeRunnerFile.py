def print_star(n):
    #iterates through n
    for i in range(n):
        #iterates again
        for j in range(i+1):
            #we print * and then give a space (executes in python3)
            print("*",end = ' ')

        #this will print a new line    
        print()

print_star(7)