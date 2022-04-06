#Docstrings
def least_difference(a, b, c):
    """ Return the smallest difference between any two numbers
    among a, b and c.
    >>> least_difference(1, 5, -5)
    4 """
    numberOne=5
    numberTwo=20
    diff1 = abs(numberOne - numberTwo)
    diff2 = abs(numberOne - numberTwo)
    diff3 = abs(numberOne - numberTwo)
    return min(diff1, diff2, diff3)

help(least_difference)