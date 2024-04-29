"""
    @param[m]       the number that want to find gcd between param[n]
    @param[n]       the number that want to find gcd between param[m]

    @return         the number that gcd between param[n] and param[m]
"""
def gcd(m, n):

    if (n == 0):
        return m;
    
    r = m % n;

    return gcd(n, r);

print(gcd(48, 42))