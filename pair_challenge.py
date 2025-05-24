"""Pair challenge

given_list = [2, 4, 6, 8, 10]

Expected result:
(2,4) (4,6) (6,8) (8,10)
(4,6) (6,8) (8,10)
(6,8) (8,10)
(8,10)
"""

def print_pairs(user_list: list):
    """Print the content of a list formatted by pairs of elements
    Args:
        user_list (list): elements ready to be processed
    """
    for i in range(len(user_list)):
        for j, number in enumerate(user_list):
            if (j + 1) < len(user_list):
                print((number, user_list[j + 1]), end=" ")
            else:
                if len(user_list) >= 2:
                    print("\n")
                    user_list.pop(i)
                    print_pairs(user_list)

proposed_list = [2, 4, 6, 8, 10]
print_pairs(proposed_list)
