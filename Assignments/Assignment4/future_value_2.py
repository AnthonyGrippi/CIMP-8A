def print_welcome(message):
    print(message)
    print()


def calculate_future_value(monthly_investment, yearly_interest, years=20):
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years *12

    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    
    return future_value


def main():
    #display the header
    message = "Welcome to the Future Value Calculator"
    print_welcome(message)

    choice = "y"
    while choice.lower() == "y":
        monthly_investment = float(input("Enter monthly investment:\t"))
        yearly_interest = float(input("Enter yearly interest rate:\t"))
        years = int(input("Enter number of years:\t\t"))

        #Get the future value
        future_value = calculate_future_value(monthly_investment=monthly_investment, years=years, yearly_interest=yearly_interest)

        #display future value
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        #see if the user wants to calculate another
        choice = input("Continue? (y/n): ")
        print()
    
    print("Exiting the Future Value Calculator")

if __name__ == "__main__":
    main()

