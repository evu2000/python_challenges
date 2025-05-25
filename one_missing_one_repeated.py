""" Given a list of numbers from 1 to 100, one number is missing, but
this time another number is duplicated...
Could you locate both the missing and the repeated numbers?
"""

def find_missing_and_repeated(given_list: list) -> list:
    """Function that inspects an ordered list looking for missing
    and repeated elements

    Args:
        given_list (list): List to be inspected

    Returns:
        list: The list with the results (with fixes if any)
    """
    missing_found = False
    repeated_found = False
    for index, value in enumerate(given_list):
        if index != value - 1:
            print(f"Element {value - 1} is missing, adding it to the list")
            missing_found = True
            given_list.insert(index, value - 1)        
            break
    if given_list[-1] != len(given_list):
        repeated_found = True
        print(f"Element {given_list[-1]} is duplicated, removing it from list")
        given_list.pop()

    if not missing_found:
        print("No missing number found, list is OK")
    if not repeated_found:
        print("No duplicated number found, list is OK")

    return given_list

my_list = list(range(1,10))
my_list.remove(8)
my_list.append(2)

print(find_missing_and_repeated(my_list))
