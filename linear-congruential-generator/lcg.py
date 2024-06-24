MODULUS = 1033          # M, 0 < M          — the "modulus"
MULTIPLIER = 827        # A, 0 < A < M      — the "multiplier"
INCREMENT = 57          # C, 0 <= C < M     — the "increment"
SEED = 512              # X, 0 <= X < M     — the "seed" or "start value"

# X' = (A*X + C) mod M, recurrence relation
def lcg():

    global SEED
    
    SEED = (MULTIPLIER * SEED + INCREMENT) % MODULUS
    print(SEED)