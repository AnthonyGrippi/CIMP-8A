from datetime import date, time, datetime

# Date object
date_today = date.today()
print("Today is: " + str(date_today))

next_solar_eclipse = date(2024, 4, 8)
print("The next solar eclipse in the US will be: " + str(next_solar_eclipse))

right_now = datetime.now()
print("Right now: " + str(right_now))


final_project_due = datetime(2018, 5, 21, 18, 0, 0)
print("The final project is due: " + str(final_project_due))

class_start_time = time(18, 0)
print("Class starts at: " + str(class_start_time))