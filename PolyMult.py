## Ria Talwar, Honors Precalculus, February 1, 2022
## Assignment 2: Polynomial Derivatives Extensions
## Multiply polynomials

import numpy as np

def poly_multiply(coeffs1, coeffs2):
    '''
    Description: Multiply two polynomials together
    Parameters: Array coeffecients of p1, Array coeffecients of p2
    Return: Array new coefficients
    '''
    newCoeffs = [0] * (len(coeffs1) + len(coeffs2) - 1)     # Determine number of new coefficients
    for i in range(len(coeffs1)):
        for j in range(len(coeffs2)):
            x = i + j                                       # Get degree of current coeff
            newCoeffs[x] += coeffs1[i] * coeffs2[j]         # Add new value to current coeff at index
    return np.array(newCoeffs)                              # Convert to np array and return

def test():
    print(poly_multiply(np.array([0]), np.array([0])) == np.array([0]))
    print(poly_multiply(np.array([0, 1]), np.array([0])) == np.array([0, 0]))
    print(poly_multiply(np.array([1, 2]), np.array([1])) == np.array([1, 2]))
    print(poly_multiply(np.array([3, 2, 1]), np.array([1])) == np.array([3, 2, 1]))
    print(poly_multiply(np.array([1, 2]), np.array([3, 4])) == np.array([3, 10, 8]))
    print(poly_multiply(np.array([1, 2]), np.array([-3, 4])) == np.array([-3, -2, 8]))

test()
