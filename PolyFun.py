## Ria Talwar, m d, 2022
## Brief description of program

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
"""
creates a string representation of the polynomial equation
parameter: polynomial coefficient array
returns: string representation of the equation
"""
# TODO: write this function and the others, adding parameters as required
# TODO: write docstrings for all the functions using the template above
def poly_to_str(coeffs):
    '''
    Description: Creates a string representation of the polynomial equation
    Parameters: Array coeffecients
    Return: String equation
    '''
    equation = ''
    for i in range(len(coeffs)):
        if coeffs[i] != 0:
            if i == 0:
                equation = str(coeffs[i])
            else:
                equation = '(' + str(coeffs[i]) + ')x^' + str(i) + " + " + equation
    return equation

def poly_eval(coeffs, inputs):
    '''
    Description:
    Parameters: Void
    Return: Array outputs
    '''
    outputs = np.array([])
    return outputs

def poly_diff():
    '''
    Description:
    Parameters: Void
    Return: Array
    '''
    myArray = np.array([])
    return myArray

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


def test():
    print("poly_to_str")
    test_poly_to_str()


def run():
    ## INPUTS

    # Coefficients of polynomial from 0th to nth; eventually this will be replaced
    # by a call to get_coeffs()
    coeffs = np.array([2, -10, .5, .25])

    # Parameters for plotting
    xMin = -10
    xMax = 10
    numPts = 200

    ## CALCULATIONS
    # Create a string to display the equation of the polynomial
    # Use a loop to do this so it works for any degree polynomial
    eqn = "P(x) = a0 + a1*x + ..."

    # Generate the points on the curve over the domain xMin to xMax
    # Use a loop through the coeffecients so it works for any degree,
    # but also use array operations so you DON'T have to loop through the x-values
    x = np.array([1, 2, 3, 4, 5]);
    y = x + 1;

    ## OUTPUT
    print(eqn)  # Print the equation to the console

    # Plot the polynomial
    #plt.plot(x,y)
    #plt.grid(True)
    #plt.show()
    # plt.ylim(-5, 5)   # Uncomment if you need to adjust the y-scale of your plot

test()
