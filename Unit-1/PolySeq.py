# Ria Talwar, Honors Precalculus, Octber 29, 2021
# A program to generate terms and sum of a series
import numpy as np

def sequence_terms(coefficients, numTerms):
    ''' Description: Calculate the first n terms of a polynomial sequence
        Parameters: List of coefficients, Integer number of terms
        Return: List of terms '''
    terms = []
    # Calculate each term
    for k in range(1, numTerms + 1):
        pk = 0
        # Calculate each element of the term
        for i in range(len(coefficients)):
            pk += coefficients[i] * k ** i
        terms.append(pk)
    return terms


def sequence_sum(coefficients, n):
    ''' Description: Calculate the sum of the first n terms of a polynomial sequence
        Parameters: List of coefficients, Integer number of terms
        Return: Float sum of sequence '''
    deg = len(coefficients)
    # Must have at least one coefficient but check for the rest
    sum = coefficients[0] * n
    if deg > 1:
        sum += coefficients[1] * (n + 1) * n / 2
    if deg > 2:
        sum += coefficients[2] * n * (n + 1) * (2 * n + 1) / 6
    if deg > 3:
        sum += coefficients[3] * n ** 2 * (n + 1) ** 2 / 4
    return sum


def test():
    ''' Description: Run test cases for sequence_terms and sequence_sum functions
        Parameters: Void
        Return: Void '''
    print(sequence_terms([-1.0, 4.0, -3.0, 0.5], 5) == [0.5, -1.0, -2.5, -1.0, 6.5])
    print(sequence_sum([-1.0, 4.0, -3.0, 0.5], 15) == 3945)
    print(sequence_terms([1, 1, 1, 1], 5) == [4.0, 15.0, 40.0, 85.0, 156.0])
    print(sequence_sum([1, 1, 1, 1], 5) == 300)
    print(sequence_terms([6, -2], 4) == [4, 2, 0, -2])
    print(sequence_sum([6, -2], 4) == 4)
    print(sequence_terms([1, -2, 1], 5) == [0, 1, 4, 9, 16])
    print(sequence_sum([1, -2, 1], 5) == 30)
    print(sequence_terms([1, -1, 3, -2], 6) == [1, -5, -29, -83, -179, -329])
    print(sequence_sum([1, -1, 3, -2], 6) == -624)


def main():
    print("This program will calculate terms and a sum from a polynomial sequence.\n" +
          "A polynomial sequence has an explicit equation of the form:\n" +
          "Pk = a0 + a1*k^1 + a2*k^2 +a3*k^3 + ... + an*k^n\n" +
          "The value of n is called the degree of the sequence.\n" +
          "Note: This program only works for sequences of degree 3 or less.")

    # INPUT
    # Get and store coefficients in np array
    coefficients = []
    i = 0
    while i < 4:
        inp = input("Enter your value for a" + str(i) + " or hit ENTER to stop: ")
        try:
            coefficients.append(float(inp))
            i += 1
        # Prevent user from causing an error with invalid input
        except:
            if inp == "" and i > 0:
                break
            else:
                continue
    coefficients = np.array(coefficients)
    numTermsDisplay = int(input("How many terms do you want to see? "))
    numTermsSum = int(input("How many terms do you want in your sum? "))

    # CALCULATIONS
    terms = sequence_terms(coefficients, numTermsDisplay)
    sum = sequence_sum(coefficients, numTermsSum)

    # RESULTS
    # Print out sequence string
    print("For the sequence defined by Pk = " + str(coefficients[0]), end="")
    for i in range(1, len(coefficients)):
        if i < len(coefficients) and coefficients[i] != 0:
            print(" + " + str(coefficients[i]) + "k^" + str(i), end="")

    # Print out the reqested terms
    print("\nThe first 5 terms are:")
    strTerms = [str(t) for t in terms]
    s = ", "
    print("{ " + s.join(strTerms) +" }")
    print("The sum of the first", numTermsSum, "terms is:", sum)

main()
