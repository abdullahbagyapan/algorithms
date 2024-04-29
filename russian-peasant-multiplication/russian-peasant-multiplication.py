import math


"""
    @param[n] the number that we want to keep it small
    @param[m] the result without remainders
    @param[x] the remainder from previous calculation

    @return value of multiplication
"""
def multiply(n, m, x = 0):

    if (n == 1):
        return m + x

    if (n % 2 == 0):
        return multiply(n / 2, m * 2, x)

    return multiply(math.floor(n / 2), m * 2, x + m)


print(multiply(13,20))



"""
Russian peasant multiplication (a.k.a ancient Egyptian multiplication) is a systematic method
for multiplying two numbers that does not require the multiplication table,
only the ability to multiply and divide by 2, and to add.


E.g

13 × 238 = ? 

13 		238
6       476     (remainder discarded)
3 		952
1       1904    (remainder discarded)
_____________________________________

476     (remainder)
1904    (remainder)
1904    (latest value of 'm')
+_____

= 3094
"""