# import calendar
#
# print(calendar.calendar(2022))


from datetime import datetime, timedelta, date, time

print(date.today())
print(datetime.now())

now = datetime.now()

print(f"{now: %A, %B %d %Y}")
print("\n===========================\n")

dd = datetime(year=2022, hour=23, day=5, month=2, minute=45)
print(dd)
print("\n=============================\n")
ddd = datetime.strptime("2022/10/10 10:30", "%Y/%m/%d %H:%M")
print(ddd)

x = ddd + timedelta(days=10)
print(ddd.day)
print(x.day)