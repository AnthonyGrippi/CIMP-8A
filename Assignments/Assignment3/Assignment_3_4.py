sport = "hockey"
city = "Anaheim"
team = ""

if sport == "baseball":
    if city.lower() == "anaheim":
        team = "Dodgers"
elif sport == "hockey":
    if city.lower() == "anaheim":
        team = "Ducks"
    if city.lower() == "los angeles":
        team = "Kings"

print("The " + sport + " team is " + city + " is the " + team)
