## Ria Talwar, Honors Precalculus, Octber 5, 2021
## A program to generate terms of a geometric sequence
import numpy as np

def calculate(ratio, term1, numTerms):
    ''' Parameters: Float ratio of series, Float first term, Integer number of terms
        Return: String sequence of terms, String equation of series
        Description: Calculate the first n terms of a geometric series '''
    # Generate the terms
    indices = np.arange(1, numTerms + 1)
    terms = term1 * ratio ** (indices - 1)

    # Make a string representation of the sequence
    sequenceString = "{ "
    i = 0
    while i < numTerms:
        sequenceString += str(terms[i]) + ", "
        i += 1
    sequenceString += "... }"

    # Make a string representation of the explicit formula
    equationString = "g_k = " + str(term1) + " * " + str(ratio) + " ^ (k - 1)"
    return sequenceString, equationString


def main():
    # INPUT
    ratio = float(input("Enter the ratio: "))
    term1 = float(input("Enter the first term: "))
    numTerms = float(input("Enter the number of terms: "))

    # CALCULATIONS
    sequenceString, equationString = calculate(ratio, term1, numTerms)

    # OUTPUT
    print("The first", numTerms, "terms of", equationString, "are:")
    print(sequenceString)

main()
