import datetime as dt


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)
if year == 2025:
    print('fight for getting job')


# date time object of our own
date_of_birth = dt.datetime(year=1993, month=10, day=13, hour=9, minute=8, second=0)
print(date_of_birth)
