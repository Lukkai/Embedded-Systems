import time
import os
import keyboard


def set_clock(timer):
    time.sleep(0.1)
    while not keyboard.is_pressed("enter"):     #oczekiwanie na enter, aby zmienic godzine
        time.sleep(0.09)
        os.system("cls")
        if keyboard.is_pressed("up"):           #strzalka do gory, zwieksza czas o 1 min
            timer = timer + 60
        if keyboard.is_pressed("down"):         #strzalka do dolu, zmniejsza czas o 1 min
            timer = timer - 60
        set_time = timer
        my_time = time.gmtime(set_time)
        # print(my_time)
        print(f"{my_time[3]}:{my_time[4]}:{my_time[5]}")
    return set_time
    


def timer_clock():
    timer = time.time()
    time_counter = 0
    while True:
        time.sleep(0.1)
        time_counter = time_counter + 1
        if time_counter == 10: 
            timer = timer + 1
            time_counter = 0
        os.system("cls")                        #odswiezanie konsoli poprzez regularne czyszczenie jej co 0.1s
        if keyboard.is_pressed("enter"):        #klikniecie enter pozwala na edycje godziny
            timer = set_clock(timer)
            time_counter = 0
        clock = time.gmtime(timer)
        print(f"{clock[3]}:{clock[4]}:{clock[5]}")
        if keyboard.is_pressed("esc"):          #wcisniecie escape konczy program
            return False

timer_clock()