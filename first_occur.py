""" Recursive search function without using initial position parameter """

my_array = [1, 3, 4, 2, 4]

def first_occur(array: list, target: int) -> int:
    ''' Recursive function that looks for a target number within a given list

    Args:
        array (list): The array to be examined
        target (int): The target to be found

    Returns:
        int: Target's position if found, -1 otherwise
    '''
    if not array:
        return -1
    if array[0] == target:
        return 0
    else:
        result = first_occur(array[1:], target)
        if result != -1:
            return result + 1
        else:
            return -1

print(first_occur(my_array, 2))
