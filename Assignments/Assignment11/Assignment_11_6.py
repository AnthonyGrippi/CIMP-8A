from datetime import datetime

sun_set = datetime(2018, 1, 1, 17, 12, 0)

year = sun_set.year
month = sun_set.month
day = sun_set.day
hour = sun_set.hour
minute = sun_set.minute
second = sun_set.second

time_now = datetime.now()
print("The time is: " + str(time_now.hour) + ":" + str(time_now.minute))
if (time_now.hour > hour or (time_now.hour == hour) and (time_now.minute > minute)):
    print("The sun has set today")

else:
    print("The sun has not set yet")