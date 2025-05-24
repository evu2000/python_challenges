"""Given an integer array nums, return True if any value appears
at least twice in the array, and return False if every element
is distinct
"""

given_array = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

def repeated(given_list: list):
    """Function that returns True if any element is duplicated
    in a list

    Args:
        given_list (list): List to be evaluated

    Returns:
        _type_: Boolean: True if any element is repeated, False otherwise
    """
    for element in given_list:
        duplicated = given_list.count(element)
        if duplicated > 1:
            return True
    return False

print(f"Given array: {given_array}\nElements duplicated?: {repeated(given_array)}")
