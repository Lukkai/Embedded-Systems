class Clock():
    hour = 18
    min = 50
    sec = 0
    time = "{:02d}:{:02d}:{:02d}".format(hour, min, sec)
    sleep = 180
 
    def __init__(self):
        pass

    def SetTime(self, hour = 0, min = 0):
        pass

    def Counter(self):
        pass

    def SetSleep(self, sleep = 0):
        pass

    def Alarm(self):
        pass

if __name__ == '__main__':
    clock = Clock()
    clock.SetTime()
    clock.Counter()
    clock.SetSleep()
    clock.Alarm()
    # print(clock.time)