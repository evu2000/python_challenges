""" Given a target number, find the two required numbers among
    the elements of a list whose sum corresponds to it.
"""

def search_in_list(given_list: list, target: int) -> list:
    """Function that searches for the first pairs of elements in a list that sum the target value

    Args:
        given_list (list): List with the admitted values
        target (int): Target value

    Returns:
        list: List containing the first matching pair values
    """
    
    pair_values = []
    for element in [element for element in given_list if element <= target]:
        difference = target - element
        if difference in given_list and difference != element:
            pair_values.append(given_list.index(element))
            pair_values.append(given_list.index(difference))
            return pair_values
    return pair_values

my_list = [2, 3, 6, 8, 12, 15]
TARGET = 9

positions = search_in_list(my_list, TARGET)

print(f"Original list: {my_list} - Target: {TARGET}")
if len(positions) == 0:
    print(f"No pair of values matches {TARGET}")
else:
    print(f"Position: [{positions[0]}] Value: {my_list[positions[0]]}")
    print(f"Position: [{positions[1]}] Value: {my_list[positions[1]]}")
