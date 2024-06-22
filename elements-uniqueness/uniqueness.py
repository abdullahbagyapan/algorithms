def isUnique(list):
    """
    Check whether all the elements in the list are unique.

    :param list:                                    The list

    :return True if its unique, otherwise Flase     The status of uniqueness
    """

    # the nature of sets is all elements are unique, there is no chance to duplication
    set_list = set(list)

    if (len(list) != len(set_list)):
        return False
    
    return True
