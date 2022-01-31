## Ria Talwar, m d, 2022
## Find the derivative of a polynomial

'''
1.  Add to the program outlined below so it prints the equation of the polynomial
    and makes a plot of the curve.

2.  Add to this program so that it calculates the derivative of the given polynomial,
    displays the equation of the derivative, and plots the derivative on the
    same graph as the original function.

3.  Add to this program so that it is interactive – it prompts the user
    each time to enter the coefficients of the polynomial.

4.  Think carefully about writing additional functions: do not duplicate the
    tasks that can be accomplished by functions that already exist
    (e.g. don't write a diffToStr function!)
'''

## Import Modules
import numpy as np
import matplotlib.pyplot as plt

## FUNCTIONS

def poly_to_str(coeffs):
    '''
    Description: Creates a string representation of the polynomial equation
    Parameters: Array coeffecients
    Return: String equation
    '''
    equation = ''
    for i in range(len(coeffs)):
        if coeffs[i] != 0:  # Skip if coefficient is 0
            if i == 0:      # No x or () if coef for x^0
                string = str(coeffs[i])
            else:
                string = '(' + str(coeffs[i]) + ')x^' + str(i)

            if len(equation) != 0:    # No plus if length of equation == 0
                equation = string + ' + ' + equation
            else:
                equation = string
    return equation

def poly_eval(coeffs, inputs):
    '''
    Description: Calculates the outputs of the polynomial.
    Parameters: Array coefficients, Array inputs
    Return: Array outputs
    '''
    outputs = coeffs[0] * inputs ** 0   # Coef for x^0
    for i in range(1, len(coeffs)):     # Iterate over remaining coeffecients
        outputs = outputs + coeffs[i] * inputs ** i
    return outputs

def poly_diff(coeffs):
    '''
    Description: Find the derivative of a polynomial
    Parameters: Array coeffiecients of polynomial
    Return: Array coefficients of derivative
    '''
    deriv = coeffs * np.arange(len(coeffs))
    deriv = np.delete(deriv, 0)
    return deriv

def get_coeffs():
    '''
    Description:
    Parameters: Void
    Return: Array coefficients
    '''
    coeffs = np.array([])
    return coeffs


def test_poly_to_str():
    print(poly_to_str(np.array([1, -2, 3])) == '(3)x^2 + (-2)x^1 + 1')
    print(poly_to_str(np.array([1])) == '1')
    print(poly_to_str(np.array([1, 2, 3, 4])) == '(4)x^3 + (3)x^2 + (2)x^1 + 1')
    print(poly_to_str(np.array([1, 2])) == '(2)x^1 + 1')
    print(poly_to_str(np.array([1, -2, 3, -4, 5])) == '(5)x^4 + (-4)x^3 + (3)x^2 + (-2)x^1 + 1')
    print(poly_to_str(np.array([1, -2, 0, -4, 0])) == '(-4)x^3 + (-2)x^1 + 1')
    print(poly_to_str(np.array([0])) == '')
    print(poly_to_str(np.array([1, -2, 0, 0, 5])) == '(5)x^4 + (-2)x^1 + 1')
    print(poly_to_str(np.array([0, 0, 5])) == '(5)x^2')

def test_poly_eval():
    print(poly_eval(np.array([0]), np.array([1, 2, 3])) == np.array([0, 0, 0]))
    print(poly_eval(np.array([0, 1]), np.array([1, 2, 3])) == np.array([1, 2, 3]))
    print(poly_eval(np.array([1, 2]), np.array([1, 2, 3])) == np.array([3, 5, 7]))
    print(poly_eval(np.array([3, 2, 1]), np.array([1, 2, 3])) == np.array([6, 11, 18]))

def test_poly_diff():
    print(poly_diff(np.array([0])) == np.array([]))
    print(poly_diff(np.array([0, 1])) == np.array([1]))
    print(poly_diff(np.array([1, 2])) == np.array([2]))
    print(poly_diff(np.array([3, 2, 1])) == np.array([2, 2]))
    print(poly_diff(np.array([3, 2, 1, -3])) == np.array([2, 2, -9]))

def test():
    print('poly_to_str')
    test_poly_to_str()
    print('\npoly_eval')
    test_poly_eval()
    print('\npoly_diff')
    test_poly_diff()


def run():
    ## INPUTS

    # Coefficients of polynomial from 0th to nth; eventually this will be replaced
    # by a call to get_coeffs()
    coeffs = np.array([0, 0, 1])

    # Parameters for plotting
    xMin = -10
    xMax = 10
    numPts = 200

    ## CALCULATIONS
    # Create a string to display the equation of the polynomial
    eqn = poly_to_str(coeffs)

    # Generate the points on the curve over the domain xMin to xMax for polynomial and derivative
    x = np.linspace(xMin, xMax, numPts)
    y = poly_eval(coeffs, x)

    deriv = poly_diff(coeffs)
    yd = poly_eval(deriv, x)

    ## OUTPUT
    print(eqn)  # Print the equation to the console

    plt.plot(x, y)  # Plot the polynomial
    plt.plot(x, yd) # Plot the derivative
    plt.grid(True)
    plt.show()
    # plt.ylim(-5, 5)   # Uncomment if you need to adjust the y-scale of your plot

test()
