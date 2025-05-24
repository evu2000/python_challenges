"""Define a function that converts fluid ounces to milliliters
knowing that 1 fluid ounce is equal to 29.57353 milliliters.
For example, I was to call your function with foo(1) I would get
an output of 29.57353. If I called it with  foo(5) I would get
147.86765, and so on."""

def ounce_to_ml(ounces: float) -> float:
    """Function that converts ounces to ml

    Args:
        ounces (float): Ounces to be converted

    Returns:
        float: Equivalent amount in ml.
    """
    return ounces * 29.57353

onzas = input("Enter ounce/s amount: ")
print (f"{onzas} ounce/s are equal to {ounce_to_ml(float(onzas))} ml.")
