from datetime import datetime

today = datetime.today()
last_day_of_class = datetime(2021, 12, 21)
time_span = last_day_of_class - today

print("Days left in class:", time_span.days)