def mergesort(A):
    """
    Sort a list

    :param A:                   The list

    :return sorted_list:        The sorted list
    """

    def merge(A, left_index, mid_index, right_index):
        """
        Merge a list

        :param left_index:          The index of left partition
        :param mid_index:           The index of mid
        :param right_index:         The index of right partition

        :return :       The merged list
        """

        n1 = mid_index - left_index + 1
        n2 = right_index - mid_index

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = A[left_index + i]

        for j in range(0, n2):
            R[j] = A[mid_index + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = left_index  # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            A[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            A[k] = R[j]
            j += 1
            k += 1


    def sort(A,left_index, right_index):

        if right_index <= left_index:
            return

        mid_index = left_index + (right_index - left_index) // 2

        sort(A, left_index, mid_index)
        sort(A, mid_index + 1, right_index)

        merge(A, left_index, mid_index, right_index)


    sorted_list = sort(A, 0, len(A) - 1)

    return sorted_list


A = [9, 8, 6, 5, 2, 13, 12, 33, 0, 1, 12]

mergesort(A)

print(A)