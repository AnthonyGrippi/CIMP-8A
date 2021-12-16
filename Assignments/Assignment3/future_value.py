print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    monthly_investment = float(input("Enter monthly investment:\t"))
    yearly_investment_rate = float(input("Enter yearly investment rate:\t"))
    years = int(input("Enter the amount of years:\t"))

    monthly_investment_rate = yearly_investment_rate / 12 / 100
    months = years * 12

    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_investment_rate
        future_value += monthly_interest_amount

    print("Future value:\t\t\t\t" + str(round(future_value, 2)))
    print()

    choice = input("Continue? (y/n): ")
    print()

print("The program has ended")