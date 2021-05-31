#zad1
#Iterujac po elementach listy wypisz na ekran wartość elementu i jego liczbę porządkową
DATA = ['a', 'b', 'c'] 
slownik = {}
for i,value in enumerate(DATA):
    slownik[i] = value
print(slownik)



#zad2
#Scal/Przyporzadkuj elementy listy DATA i values: 
values = [1, 2, 3]
dic = {}
for i in range(len(DATA)):
        dic = {DATA[i]:values[i]}
print(dic)

zip(DATA,values)

#zad3
payload = [ 
{"marka": "Audi", "typ": "sedan", "model": "A3", "predkosc_max": "240"}, 
{"marka": "BMW","typ": "sedan","model": "E60","predkosc_max": 200}, 
{"marka": "BMW","typ": "sedan","model": ""}, 
{"marka": "Opel","typ": "sedan","model": "Astra","predkosc_max": 220} 
] 
#1 Utwórz listę z wszystkimi modelami samochodów, które jadą szybciej niż 215 km/h. 
speed = [i['marka'] for i in payload if "predkosc_max" in i if int(i["predkosc_max"]) > 215]
print(speed)

# speed = [next(filter(lambda auto: auto['marka'], payload)) for i in payload if "predkosc_max" in i if int(i["predkosc_max"]) > 215]
# print(speed)


# if (payload(each["predkosc_max"]) > 215):
#     # speed.append(each)
#     print(payload[each])




# y = [1,2,3,4]
# x = ["a","b","c","d"]

# # This below is a brute force method
# obj = {}
# for i in range(len(y)):
#     obj[y[i]] = x[i]
# print(obj)

# # Recursive approach 
# obj = {}
# def map_two_lists(a,b,j=0):
#     if j < len(a):
#         obj[b[j]] = a[j]
#         j +=1
#         map_two_lists(a, b, j)
#         return obj
      


# res = map_two_lists(x,y)
# print(res)

# Both the results should print

# {1: 'a', 2: 'b', 3: 'c', 4: 'd'}  