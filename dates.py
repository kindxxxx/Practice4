import datetime

now = datetime.datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)

print("next task.")


import datetime

now = datetime.datetime.now()

weekday = now.strftime("%A")
short_date = now.strftime("%d-%m-%Y")

print(weekday)
print(short_date)
