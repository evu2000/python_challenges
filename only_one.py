""" Returns the single non-repeating element in a list.
    2 flavours here: using COUNT and using DICTIONARY """

my_list = [1,1,2,2,3,4,4,4,5,5]

def non_repeating_count(a_list: list) -> int:
    for element in a_list:
        if a_list.count(element) == 1:
            return element
    return 0

print(non_repeating_count(my_list))

def non_repeating_dict(a_list: list) -> int:
    dictionary = {}
    for element in a_list:
        if element not in dictionary:
            dictionary.update({element: a_list.count(element)})
    element = [clave for clave, valor in dictionary.items() if valor == 1]
    return element[0]

print(non_repeating_dict(my_list))
