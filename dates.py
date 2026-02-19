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


import datetime

text = "2026-03-15 09:00"
dt = datetime.datetime.strptime(text, "%Y-%m-%d %H:%M")

print(dt)
print(dt.hour)
print(dt.minute)


print("next task")



import datetime

today = datetime.date.today()

after_30_days = today + datetime.timedelta(days=30)
before_10_days = today - datetime.timedelta(days=10)

print(today)
print(after_30_days)
print(before_10_days)


print("next task")



import datetime

start = datetime.date(2026, 1, 1)
end = datetime.date(2026, 2, 1)

difference = end - start

print(difference.days)
