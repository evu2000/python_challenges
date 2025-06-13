""" Palindrome Exercise """

def is_palindrome(string: str) -> bool:
    """Function that analyzes if a string is a palindrome or not

    Args:
        string (str): String to be analyzed

    Returns:
        bool: Returns 'True' if is palindrome, 'False' otherwise
    """
    reversed_string = ""
    for character in string[::-1]:
        reversed_string += character
    return True if string == reversed_string else False

MY_STRING = "racecar"
print(is_palindrome(MY_STRING))
