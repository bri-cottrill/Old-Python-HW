"""
02/23/19 Week 6 HW - Time
Return the number of seconds since midnight for events in access_log.
"""

import datetime
from datetime import timedelta
import re

"""Use regex to find and extract the time. Yield the time and number of seconds since midnight."""
def from_midnight(file):
    for line in file:
        time_match =  re.findall('\[\d\d/\D\D\D/\d\d\d\d:(\d\d:\d\d:\d\d)\s', line)
        this_time = datetime.datetime.strptime(time_match[0],'%H:%M:%S').time()
        total_secs = timedelta(hours = this_time.hour, minutes = this_time.minute, seconds = this_time.second).total_seconds()
        yield "The number of seconds from midnight to " + str(this_time) + " is " + str(total_secs)

open_log = open('/etc/httpd/logs/access_log')
secs_gen = from_midnight(open_log)
for _ in range(10):
    print(next(secs_gen))
            
