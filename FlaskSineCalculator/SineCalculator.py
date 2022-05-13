# Ria T, Honors Precalculus, May 18, 2022
# Special Topics Project 1: Sine Calculator
# Calculates the sine of a value using a polynomial approximation of the sine function

import math
import matplotlib
import numpy as np

PI = np.pi  # Store the value of pi in a global variable
DEGREE = 15 # Set degree of accuracy for polynomial approximation

# Just for fun, here's the recursive implementation of the factorial function
# Using recursion gives you a really simple and elegant solution,
# and it's more interesting than a regular loop, even though that can be safer
# If you enter a really large number, you could end up with a stack overflow error
def factorial(n):
    '''
    Description: Calculate the factorial of a given number
    Parameters: Integer n
    Return: Integer n factorial
    '''
    if n < 0:   # Catch invalid input
        return -1
    if n == 0:  # Base case
        return 1
    return n * factorial(n - 1)


def get_radians():
    '''
    Description: Get number radians from user
    Parameters: void
    Return: Double radians
    '''
    while True:
        inp = input("Enter a number of radians within the domain [0, PI/4]: ")
        try:
            inp = float(inp)
            return inp
        except: # Catch invalid input
            print("Invalid input. Please enter valid number within the correct domain.")


def sin(x):
    '''
    Description: Calculate the sine of a number using a polynomial approximation
    Parameters: Double x radians
    Return: Double sine of x radians
    '''
    # Make sure x is in domain [0, 2PI)
    if x >= 2 * PI:
        x -= int(x / (2 * PI)) * 2 * PI
    if x < 0:
        x += int(x / (2 * PI) - 1) * -2 * PI

    if x <= PI / 4 and x >= 0:
        return sin_converted(x)             # [0, PI/4]
    if x <= PI / 2 and x > PI / 4:
        return cos_converted(PI / 2 - x)    # (PI/4, PI/2]
    if x <= 3 * PI / 4 and x > PI / 2:
        return cos_converted(x - PI / 2)    # (PI/2, 3PI/4]
    if x <= PI and x > 3 * PI / 4:
        return sin_converted(PI - x)        # (3PI/4, PI]
    return -1 * sin(x - PI)                 # (PI, 2PI)


def cos(x):
    '''
    Description: Calculate the cosine of a number using the sine function
    Parameters: Double x radians
    Return: Double cosine of x radians
    '''
    # Make sure x is in domain [0, 2PI)
    if x >= 2 * PI:
        x -= int(x / (2 * PI)) * 2 * PI
    if x < 0:
        x += int(x / (2 * PI) - 1) * -2 * PI

    if x <= PI / 4 and x >= 0:
        return cos_converted(x)             # [0, PI/4]
    if x <= PI / 2 and x > PI / 4:
        return sin_converted(PI / 2 - x)    # (PI/4, PI/2]
    if x <= 2 * PI and x > 7 * PI / 4:
        return cos_converted(2 * PI - x)    # (7PI/4, 2PI]
    if x <= 7 * PI / 4 and x > 3 * PI / 2:
        return sin_converted(2 * PI - x)    # (3PI/2, 7PI/4]
    return -1 * cos(x + PI)                 # (PI/2, 3PI/2]


def sin_converted(x):
    '''
    Description: Calculate the sine of a number using a polynomial approximation
    Parameters: Double x radians in domain [0, PI/4]
    Return: Double sine of x radians
    '''
    sine = 0
    for i in range(1, DEGREE + 1, 2):
        # use below formula to get odd degrees, evens are always 0
        term = 1 / factorial(i) * x ** i
        if (i + 1) % 4 == 0:
            term *= -1
        sine += term
    return sine


def cos_converted(x):
    '''
    Description: Calculate the cosine of a number using the sine function
    Parameters: Double x radians in domain [0, PI/4]
    Return: Double cosine of x radians
    '''
    sinesqrd = sin(x) ** 2
    cosine = math.sqrt(1 - sinesqrd)
    return cosine


def tan(x):
    '''
    Description: Calculate the tangent of a number using the sine function
    Parameters: Double x radians
    Return: Double tangent of x radians
    '''
    sine = sin(x)
    cosine = cos(x)
    if cosine != 0:     # Catch undefined case
        return sine / cosine
    return "undefined"


def test():
    '''
    Description: Test functions
    Parameters: void
    Return: void
    '''
    # TODO: WRITE TEST CASES FOR SINE, COSINE, AND TANGENT (AND FACTORIAL IG)
    print("SINE TESTS")
    print("sin(0) = " + str(sin(0)))
    print("sin(PI/4) = " + str(sin(PI/4)))
    print("sin(PI/2) = " + str(sin(PI/2)))
    print("sin(3PI/4) = " + str(sin(3*PI/4)))
    print("sin(PI) = " + str(sin(PI)))
    print("sin(5PI/4) = " + str(sin(5*PI/4)))
    print("sin(3PI/2) = " + str(sin(3*PI/2)))
    print("sin(7PI/4) = " + str(sin(7*PI/4)))
    print("sin(2PI) = " + str(sin(2*PI)))
    print("sin(5PI/2) = " + str(sin(5*PI/2)))
    print("sin(-PI/2) = " + str(sin(-PI/2)))

    print("\nCOSINE TESTS")
    print("cos(0) = " + str(cos(0)))
    print("cos(PI/4) = " + str(cos(PI/4)))
    print("cos(PI/2) = " + str(cos(PI/2)))
    print("cos(3PI/4) = " + str(cos(3*PI/4)))
    print("cos(PI) = " + str(cos(PI)))
    print("cos(5PI/4) = " + str(cos(5*PI/4)))
    print("cos(3PI/2) = " + str(cos(3*PI/2)))
    print("cos(7PI/4) = " + str(cos(7*PI/4)))
    print("cos(2PI) = " + str(cos(2*PI)))
    print("cos(5PI/2) = " + str(cos(5*PI/2)))
    print("cos(-PI/2) = " + str(cos(-PI/2)))


def run():
    '''
    Description: Output approximate sine using user input
    Parameters: void
    Return: void
    '''
    # INPUT
    # TODO: IMPROVE INSTRUCTIONS
    print("Instructions:\nThis program will output the sine, cosine, and tangent of a given number of radians."
        + "Enter a value to recieve the sine, cosine, and tangent of that value.\n")

    x = get_radians()
    print()

    # PROCESSING
    sine = sin(x)
    cosine = cos(x)
    tangent = tan(x)

    # OUTPUT
    print("sin(" + str(x) + ") = " + str(sine))
    print("cos(" + str(x) + ") = " + str(cosine))
    print("tan(" + str(x) + ") = " + str(tangent))
