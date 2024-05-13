def quicksort(A):
    """
    Sort a list

    :param A:       The list
    """

    def divide_and_get_pivot_last_index():

        pivot = A[-1] # the last element
        pivot_index = len(A) - 1

        j = 0 # temporary pivot index
        for i in range(len(A) - 1):

            if A[i] <= pivot:

                A[i], A[j] = A[j], A[i] # swap
                j += 1

        A[j], A[pivot_index] = A[pivot_index], A[j]

        return j


    if (len(A) <= 2):
        return A
    
    pivot_last_index = divide_and_get_pivot_last_index()

    partition_1 = quicksort(A[:pivot_last_index])
    partition_2 = quicksort(A[pivot_last_index:])

    return partition_1 + partition_2


A = [9, 8, 6, 5, 2, 13, 12, 33, 0, 1, 12]

sorted_list = quicksort(A)

print(sorted_list)