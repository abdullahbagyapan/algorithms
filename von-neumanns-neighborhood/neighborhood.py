def calculate(n):
    """
    Returns how many one-by-one squares are there after param[n] iterations.
    ### more detailed information can be found by searching as "Von Neumann neighborhood"

    :param n:                                       The iteration number

    :return total_square_number:                    The total number of one-by-one squares
    """

    return pow(n, 2) + pow(n + 1, 2)


"""
Iteration Number        -       Total Squares Number
____________________________________________________
        0               -               1
        1               -             4 + f(0)
        2               -             8 + f(1)
        3               -            12 + f(2)
        ...             -               ...
        ...             -               ...
        
        n               -            4*n + f(n-1) -> (n^2 + (n + 1)^2)
"""