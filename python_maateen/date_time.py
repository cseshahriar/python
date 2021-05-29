# date and time 

# datetime
from datetime import date

print(date(2021, 5, 29))

# today
today = date.today()
print(today)

# year 
print(today.year)

# month
print(today.month)

# day
print(today.day)


# replace 
my_date = date.today()
replace_date = my_date.replace(2021, 5, 30)

print(my_date)
print(replace_date)

# date format
my_date2 = date.today()
my_date2.strftime('%d %B, %Y')
print(my_date2)


# time
from datetime import time
print('Time')
my_time = time(5, 15, 00)
print(my_time)
print(my_time.hour)
print(my_time.minute)
print(my_time.second)
print(my_time.microsecond)

replace_time = my_time.replace(21, 29, 45)
print(replace_time)

# time format
formate_time = my_time.strftime('%I:%M:%S')
print(formate_time)

# time zone
from datetime import datetime

my_today = datetime.today()
print(my_today)

my_time2 = datetime.now()
print(my_time2)

utc_date_time = datetime.utcnow()
print(utc_date_time)

# str time to date time
date_time_str = '2018-06-29 08:15:27.243860'
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)
