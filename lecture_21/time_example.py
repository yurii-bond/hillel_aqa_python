import time
from datetime import datetime


curr_time = time.time()
print(curr_time)
curr_time = time.localtime()
print(curr_time)
print(curr_time.tm_year)
print(curr_time.tm_mon)

print('asctime', time.asctime(curr_time))
print('time.ctime', time.ctime(0))

print('time.gmtime', time.gmtime(0))

print('time.localtime', time.localtime(0))

print('time.perf_counter', time.perf_counter())

print('time.process_time', time.process_time())

# time.sleep(3)

print('strftime', time.strftime('%Y-%m-%d %H:%M:%S',curr_time))

time_string = '2023-12-31 23:59:59'

format_str = '%Y-%m-%d %H:%M:%S'

time_obj = time.strptime(time_string, format_str)

print('time_obj', time_obj)

now = time.time()
print('now', now)

my_datetime = datetime.fromtimestamp(now)
print('my_datetime', my_datetime)



