def bucketsort(A):
    """
    Sort a list

    :param A:                   The list

    :return sorted_list:        The sorted list
    """

    def sign_elements(A):
        """
        Sign indecies in 'signed_bucket_list' by their(elements) value

        :param A:                   The list

        :return bucket_list:        The signed list
        """
        bucket_list = [0] * (max(A) + 1) # create a array size of maximum number in given array (A)

        for value in A:
            bucket_list[value] += 1

        return bucket_list

    
    def get_signed_elements(A):
        """
        Get signed indecies in given list

        :param A:                   The signed list

        :return sorted_list:        The sorted list
        """

        sorted_list = []

        for index, value in enumerate(A):
        
            if (value == 0):
                continue

            for j in range(value):
                sorted_list.append(index)

        return sorted_list


    signed_bucket_list = sign_elements(A)

    sorted_list = get_signed_elements(signed_bucket_list)

    return sorted_list


A = [9, 8, 6, 5, 2, 13, 12, 33, 0, 1, 12]

sorted_list = bucketsort(A)

print(sorted_list)