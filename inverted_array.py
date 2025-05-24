"""Inverted array challenge"""

given_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_array = []

for index in range(len(given_array)-1, -1, -1):
    reversed_array.append(given_array[index])

print(f"{given_array}")
print(f"{reversed_array}")
