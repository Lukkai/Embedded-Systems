import time
import os
import threading
import keyboard


t = time.time()    #utc time in seconds since 1970
now = time.gmtime(time.time()) #utc time in calculated time structure
tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = now
    
    
def seconds(x : int):
    time.sleep(x)
    return (time.time() - t)

def clock():
    return f"{tm_hour+2}:{tm_min}:{tm_sec}"

def set_clock(seth: int, setm: int, sets : int):
    tm_hour = seth-2
    tm_min = setm
    tm_sec = sets
    # print(f"{tm_hour+2}:{tm_min}:{tm_sec}" )

    # def alarm(x: int):
    #     timer = 

clock()
set_clock(2, 30, 00)

print(clock())

