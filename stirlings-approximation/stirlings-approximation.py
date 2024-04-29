import math


"""
    @param[x]       the number that wants to calculate factorial of it
    
    @return         the result of factorial
"""
def fac(x):
    
    result = 1

    # multiply on each iteration
    for i in range(x, 1, -1):
        result = result * i
    
    return result


"""
    @param[x]       the number that wants to calculate stirling's approximation of it
    
    @return         the result of stirling's approximation
"""
def stirling(x):

    result = pow((2 * math.pi * x), 1/2) * pow((x / math.e), x)
    return round(result,3)


x = 6

print("Factorial: {}".format(fac(x)))
print("Stirling Approximation: {}".format(stirling(x)))