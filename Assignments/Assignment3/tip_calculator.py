print("Tip Calculator\n")

cost_of_meal = float(input("Cost of meal: "))

print("\n15%")
print("Tip amount:\t" + str(round(cost_of_meal * .15, 2)))
print("Total amounr:\t" + str(round((cost_of_meal * .15) + cost_of_meal, 2)))

print("\n20%")
print("Tip amount:\t" + str(round(cost_of_meal * .20, 2)))
print("Total amounr:\t" + str(round((cost_of_meal * .20) + cost_of_meal, 2)))

print("\n25%")
print("Tip amount:\t" + str(round(cost_of_meal * .25, 2)))
print("Total amounr:\t" + str(round((cost_of_meal * .25) + cost_of_meal, 2)))