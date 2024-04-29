# Greatest Common Divisor

The greatest common divisor of two nonnegative, not-both-zero integers *m* and *n*, denoted gcd(m, n), is deﬁned as the largest integer that divides both *m* and *n* evenly, i.e., with a remainder of zero.

## Euclid’s algorithm

Euclid’s algorithm is based on applying repeatedly the equality

```
gcd(m, n) = gcd(n, m mod n)
```

where m mod n is the remainder of the division of m by n, until m mod n is equal to 0.

For example, gcd(60, 24) can be computed as follows:

```
gcd(60, 24) = gcd(24, 12) = gcd(12, 0) = 12.
```

### Pseudocode

```
while n != 0 do
    r = m mod n
    m = n
    n = r
return m
```