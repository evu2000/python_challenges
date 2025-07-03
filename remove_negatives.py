""" Removing negative values in a list using a single line of code """

numbers = [2, 3, -1, 13, -7, -9, 14]

print(list(value for value in numbers if value >= 0))
