from datetime import datetime, timedelta

today = datetime.today()
four_weeks = timedelta(weeks=4)
print("Today is: " + str(today))
print("Four weeks from today will be: " + str(today + four_weeks))
