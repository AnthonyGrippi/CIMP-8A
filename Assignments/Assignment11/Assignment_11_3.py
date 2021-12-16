from datetime import datetime

halloween = datetime(2020, 10, 31, 18, 0)

print(halloween.strftime("%Y-%m-%d"))
print(halloween.strftime("%m/%d/%Y"))
print(halloween.strftime("%m/%d/%y"))
print(halloween.strftime("%B %d, %Y (%A)"))
print(halloween.strftime("%B %d, %I:%M %p"))

print(halloween.strftime("%c"))
print(halloween.strftime("%x"))


