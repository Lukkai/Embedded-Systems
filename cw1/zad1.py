''' Program wyznaczający pierwiastki
    trójmianu dla przypadków rzeczywistych
'''
import math


while True:
    a = input('a=').upper() # Wczytaj a
    if a == "KONIEC":
        break
    a = float(a)
    b = float(input('b='))
    c = float(input('c='))
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-1*b + math.sqrt(delta))/(2*a)
        x2 = (-1*b - math.sqrt(delta))/(2*a)
        print('Dwa pierwiastki',x1,',',x2)
    elif delta == 0:
        x = -1*b/(2*a)
        print('Jeden pierwiastek',x)
    else:
        print('MicroPython nie osbługuje liczb zepolonych')#CPython owszem
print('Koniec')
