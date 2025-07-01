""" Generator function using YIELD """

def generator(end: int):
    """ Function that generates consecutive values until 'end'

    Args:
        end (int): Number of values to be generated

    Yields:
        (int): The generated value
    """
    for valor in range(end + 1):
        yield valor

for iteration in generator(10):
    print(iteration)
