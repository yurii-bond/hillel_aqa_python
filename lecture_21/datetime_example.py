import time
from datetime import datetime
from datetime import timezone
from datetime import date
from datetime import timedelta

from lecture_21.time_example import time_obj

print(datetime.now())
dt = datetime.now()
tz = timezone.utc
print(tz)
print(datetime.date(datetime.now()).strftime('%d-%m-%Y'))
print(datetime.time(datetime.now()).strftime('%H:%M:%S'))

# fromordinal

ordinal_day = 735365
dt = datetime.fromordinal(ordinal_day)
print(dt)

day_number = datetime.today().toordinal()
print(day_number)

print(time.localtime())

date_obj = datetime.strptime('2024-09-02', "%Y-%m-%d").toordinal()
print(date_obj)
century_obj = datetime(2000, 1, 1).toordinal()
print(century_obj)

print(date_obj - century_obj + 1)

today_date = date.today()

print(today_date)

### TIMEDELTA

td = timedelta(days=5, hours=3, minutes=30)

print(td)

td1 = timedelta(days=3)

print(td - td1)
print(td + td1)

print(td.total_seconds())

## Example

curr_time = datetime.now()


past_date = curr_time - timedelta(days=5)

time_diff = curr_time - past_date

print(curr_time)
print(past_date)
print(time_diff)

def is_diff_more_then_30_sec(time_a:datetime, time_b:datetime) -> bool:
    time_diff = time_b - time_a
    print('time diff', time_diff)
    return time_diff > timedelta(seconds=31)

time_a = datetime.now()
time_b = time_a + timedelta(seconds=30)

if is_diff_more_then_30_sec(time_a, time_b):
    print('WARNING')

