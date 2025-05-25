""" Given a list of numbers from 1 to 100, one number is missing.
Could you locate the missing number without traversing the list twice?
"""

def find_missing (given_list: list):
    """Function that looks for a missing number in an ordered list

    Args:
        given_list (list): List to be inspected
    """
    for index, value in enumerate(given_list):
        if index != value - 1:
            print(f"The missing value is {value - 1}")
            break

my_list = list(range(1,101))
my_list.remove(13)

find_missing(my_list)
