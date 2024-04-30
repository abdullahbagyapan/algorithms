"""
    @brief          Find common elements in given arrays

    @param[arr1]    the array 1
    @param[arr2]    the array 2

    @return         the common element list of given arrays
"""
def commonElements(arr1, arr2):

    i = 0  # arr1 iterator
    j = 0  # arr2 iterator

    commonElementsList = []

    while (i < len(arr1) and j < len(arr2)):
        
        if (arr1[i] == arr2[j]):
            commonElementsList.append(arr1[i])
            i += 1
            j += 1
            continue

        if (arr1[i] < arr2[j]):
            i += 1
            continue

        j += 1

    return commonElementsList

arr1 = [2,5,5,7]
arr2 = [5,5,7,7]

print(commonElements(arr1, arr2))