from datetime import date, datetime

current_year = datetime.now().year
first_day_of_spring = datetime(current_year, 3, 20)
first_day_of_summer = datetime(current_year, 6, 21)
first_day_of_fall = datetime(current_year, 9, 22)
first_day_of_winter = datetime(current_year, 12, 21)

today = datetime.now()

print("Today is: " + today.strftime("%B %d"))
if first_day_of_spring <= today < first_day_of_summer:
    print("It's Spring, time to plant flowers!")
elif first_day_of_summer <= today < first_day_of_fall:
    print("It's Summer, time to hit the beach!")
elif first_day_of_fall <= today < first_day_of_winter:
    print("It's Fall, time to rake the leaves!")
else:
    print("It's Winter season, time to hit the slopes")