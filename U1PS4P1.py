def get_amounts(years, starting, yearly, rate):
    ''' Description: Get the amount in an account for a certain number of years
        Parameters: Integer years, Float starting amount, Float yearly increase, Float rate of increase
        Return: List account value for given number of years '''
    amounts = [starting]
    for year in range(years):
        # Use previous year's value to calculate the next one
        amounts.append(amounts[-1] * (rate + 1) + yearly)
    return amounts


def main():
    # Get user information
    starting = float(input("Enter starting amount: "))
    yearly = float(input("Enter yearly amount: "))
    rate = float(input("Enter rate: "))
    years = int(input("Enter number of years: "))
    # Get data
    amounts = get_amounts(years, starting, yearly, rate)
    # Print data
    print("year | amount")
    for year in range(years + 1):
        print(year , "|", round(amounts[year], 2))


main()
