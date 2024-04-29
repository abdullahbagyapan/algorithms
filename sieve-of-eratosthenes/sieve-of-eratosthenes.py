import math

"""
    @param[n]       the number that search until it(inclusive)
    
    @return         the list of primes
"""
def primes(n):

    numbers = list(range(2, n+1))

    p = 2   # minimum prime number
    while (p <= math.floor(math.sqrt(n))):
        
        i = 2   # iteration counter
        while (p * i <= n):
            numbers[i * p - 2] = 0
            i += 1

        p += 1

    # get unmarked numbers as primes            
    return list(filter(lambda num: num != 0, numbers))


print(primes(130))
