import math

def johnson_trotter(n):
    """
    @param[n]       The number that we generate permutations of the numbers 1 to n,

    @return         The all permutations of given list


    Initialize the first permutation with <1 <2 ... <n
    while there exists a mobile integer
        find the largest mobile integer k
        swap k and the adjacent integer it is looking at
        reverse the direction of all integers larger than k
    """
    permutations = []
    permutation = list(range(1, n + 1))

    direction = [-1] * n  # -1 represents left, 1 represents right

    def update_directions(index):
        for i in range(n):
            if (permutation[i] > permutation[index]):
                direction[i] *= -1

    def swap_elements(index):
        i = permutation[index]
        j = permutation[index + direction[index]]
        
        permutation[index] = j
        permutation[index + direction[index]] = i
        #--------------
        i = direction[index]
        j = direction[index + direction[index]]

        direction[index + direction[index]] = i
        direction[index] = j

    def find_largest_mobile():
        mobile = -1
        largest_mobile_index = -1

        for i in range(n):

            # Eliminate boundary elements
            if (i + direction[i] < 0 or i + direction[i] > len(permutation) - 1):
                continue

            if (permutation[i] > mobile and permutation[i] > permutation[i + direction[i]]):
                mobile = permutation[i]
                largest_mobile_index = i

        return largest_mobile_index

    def swap_and_update_directions(index):

        update_directions(index)
        swap_elements(index)

    # First permutation
    #yield permutation
    permutations.append(list(permutation))

    while True:
        largest_mobile_index = find_largest_mobile()

        if largest_mobile_index == -1:
            break

        swap_and_update_directions(largest_mobile_index)

        #yield permutation
        permutations.append(list(permutation))
    
    return permutations

"""
n = 2
permutations = johnson_trotter(n)

for permutation in permutations:
    print(permutation)
"""