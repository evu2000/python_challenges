"""Clean a given list of elements different to the indicated
"""
my_list = [1.23, 1.45, 1.02, 1.11]

def clean(given_list: list, value: float) -> list:
    """Function that cleans a list from other values than the indicated one

    Args:
        given_list (list): Provided list to be cleaned
        value (float): Value to remain in the list

    Returns:
        list: Cleaned list
    """
    for element in given_list:
        if element != value:
            given_list.remove(element)
            clean(given_list, value)
    return given_list

print(clean(my_list, 1.23))
