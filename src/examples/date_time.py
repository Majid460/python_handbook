import time
from datetime import datetime, timedelta

# Date time format
# Using time
"""
The time module
Low-level functions for timestamps and clocks.
Works mostly with seconds since epoch (time.time() → float).
Can format time using time.strftime() and parse strings with time.strptime().
"""
time_n = time.time() # seconds since epoch time
# convert to human readable
formatted = time.strftime('%I:%M:%S', time.localtime(time_n))
print(formatted) # 21:47:27

# string to time
t_struct = time.strptime(formatted,'%H:%M:%S')
print(t_struct)

# Using date time
"""
The datetime module
High-level date and time objects.
Supports arithmetic, comparison, and formatting easily.
datetime.datetime, datetime.date, datetime.time, datetime.timedelta.
"""
now = datetime.now()
print(now) # 2025-10-02 21:54:02.899901

# formate to string
formatted = now.strftime('%I:%M:%S')
print(formatted)
# 09:54:56

# string to date time
d = datetime.strptime(formatted,'%I:%M:%S')
print(d) # 1900-01-01 09:56:02

new_dt = d + timedelta(minutes=5)
print(new_dt) #1900-01-01 10:02:06

# subtract
dif = new_dt - d
print(dif)
print(dif.total_seconds())
print(f"{dif.total_seconds()/3600:.2f}")
"""
0:05:00
300.0
0.08333333333333333
"""

# Create a specific time
t1 = datetime.strptime("10:30:15", "%H:%M:%S")
t2 = datetime.strptime("12:45:20", "%H:%M:%S")
new_time = t1 + timedelta(minutes=5)
print("t1 + 5 min:", new_time.time()) # t1 + 5 min: 10:35:15

# Compare:
if t2 > t1:
    print("t2 is later than t1")
else:
    print("t2 is earlier or same as t1")
# t2 is later than t1

diff_seconds = dif.total_seconds()
hours = int(diff_seconds // 3600)
minutes = int((diff_seconds % 3600) // 60)
seconds = int(diff_seconds % 60)
print(f"{hours}h:{minutes}m:{seconds}s")