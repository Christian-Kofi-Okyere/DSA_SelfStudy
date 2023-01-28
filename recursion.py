# To find the nth fibonacci number
#Solution - Not optimal
def fibonacci(n):           #Hint for base case: fibonacci sequence starts with (0,1,...) always
    if n == 2:             
        return 1    #base case
    elif n == 1:
        return 0   #base case
    else:
        return fibonacci(n-1) + fibonacci(n-2)  #recursive case

#print(fibonacci(4))

# Product Sum
# example [x, [y,z]] = x + 2 * (y + z) and [x, [y, [z]]] = x + 2 * (y + 3z)
def productSum (array, multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum = sum + productSum(element, multiplier + 1)
        else:
            sum = sum + element
    return sum * multiplier

#print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))

# Permutation
