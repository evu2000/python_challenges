"""Function definition challenge"""

def average(given_list: list) -> str:
    """Gets the average of the elements in a list

    Args:
        given_list (list): List containing the elements

    Returns:
        str_result (str): Formatted string returning the average (float with two decimal numbers)
    """
    number_of_elements = len(given_list)
    sum_of_elements = sum(given_list)
    result = sum_of_elements / number_of_elements
    str_result = f"{result:.2f}"
    return str_result

my_list = [1, 4, 5]

print("Average:", average(my_list))
