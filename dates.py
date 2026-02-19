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


print("next task")


import datetime

exam_date = datetime.datetime(2026, 3, 15, 9, 0, 0)

print(exam_date)
print(exam_date.year)
print(exam_date.strftime("%A"))


print("next task")