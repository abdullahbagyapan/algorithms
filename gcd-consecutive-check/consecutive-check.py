"""
    @param[m]       the number that want to find gcd between param[n]
    @param[n]       the number that want to find gcd between param[m]

    @return         the number that gcd between param[n] and param[m]
"""
def gcd(m, n):

    t = min(m, n)

    while (t > 0):

        if (m % t != 0):
            t -= 1
            continue

        if (n % t != 0):
            t -= 1
            continue

        return t


print(gcd(60, 24))