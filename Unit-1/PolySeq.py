import numpy as np

def sequence_terms(coefficients, numTerms):
    ''' Description: Calculate the first n terms of a polynomial sequence
        Parameters: List of coefficients, Integer number of terms
        Return: List of terms '''
    terms = []
    for k in range(numTerms):
        pk = 0
        for i in range(len(coefficients)):
            pk += coefficients[i] * k ** i
        terms.append(pk)
    return terms

def sequence_sum(coefficients, numTerms):
    ''' Description: Calculate the sum of the first n terms of a polynomial sequence
        Parameters: List of coefficients, Integer number of terms
        Return: Float sum of sequence '''
    return 0

def main():
    print("This program will calculate terms and a sum from a polynomial sequence.\n" +
          "A polynomial sequence has an explicit equation of the form:\n" +
          "Pk = a0 + a1*k^1 + a2*k^2 +a3*k^3 + ... + an*k^n\n" +
          "The value of n is called the degree of the sequence.\n" +
          "Note: This program only works for sequences of degree 3 or less.")

    # INPUT
    numCoef = 4
    coefficients = []
    for i in range(numCoef):
        coefficients.append(float(input("Enter your value for a" + str(i) + ": ")))
    coefficients = np.array(coefficients)
    numTermsDisplay = int(input("How many terms do you want to see? "))
    numTermsSum = int(input("How many terms do you want in your sum? "))

    # CALCULATIONS
    terms = sequence_terms(coefficients, numTermsDisplay)
    sum = sequence_sum(coefficients, numTermsSum)

    # RESULTS
    print("For the sequence defined by Pk = ", end="")
    for i in range(3):
        if coefficients[i] == 0:
            continue
        else:
            print(str(coefficients[i]) + "k^" + str(i), end="")
    print("\nThe first 5 terms are:")
    print(terms)
    print("The sum of the first", numTermsSum, "terms is:", sum)

main()
