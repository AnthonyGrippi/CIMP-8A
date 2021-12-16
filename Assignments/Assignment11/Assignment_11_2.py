from datetime import datetime

valentines_day = datetime.strptime("2/14/2020", "%m/%d/%Y")
print("Valentine's Day is:", valentines_day)

st_patricks_day = datetime.strptime("3/17/2020", "%m/%d/%Y")
print("St. Patricks Day is:", st_patricks_day)

jazz_concert = datetime.strptime("1/21/2020 19:30", "%m/%d/%Y %H:%M")
print("The faculty Jazz concert is at:", jazz_concert)