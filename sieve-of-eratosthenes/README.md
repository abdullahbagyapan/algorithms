# Sieve of Eratosthenes

**Sieve of Eratosthenes** is an ancient algorithm for finding all prime numbers up to any given limit.

It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime.

## Pseudocode

To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
2. Initially, let *p* equal 2, the smallest prime number.
3. Enumerate the multiples of *p* by counting in increments of *p* from 2*p* to *n*, and mark them in the list (these will be 2*p*, 3*p*, 4*p*, ...; the *p* itself should not be marked).
4. If current *p* is not enumerated, mark as prime number and iterate next number.