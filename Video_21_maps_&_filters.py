liczby = [2, 10, 12, 15, 20, 25, 30, 35]
print("start: ", liczby)
# MAPs
#map zwraca wynik. Map jest funkcja
# działa na kolekcjach, elementach iteracyjnych, imodyfilkue kazdy argument
def funkcja (x):
    return x + 2

wynik = map(funkcja, liczby) # dwa argumenty, 1-funkcja wczesniej stworzona, i kolekcje na którym ma pracowac(lista, slownik,
print("???: ",list(wynik))

wynik2 = map(lambda x: x+2, liczby )
print(list(wynik2)) #trzeba wydrukowac jako liste

print('')
print('................................PyMoodra........................_map in Python.......')
def seven_add(num):
    return num +7

numbers = [1,2,3,4]

print(list(map(seven_add,numbers)))

# z lambda
print("lambda_map: ", list(map(lambda x: x+7,numbers)))

# urls = ['https://www.geeksforgeeks.org', 'https://www.w3schools.com/', 'https://www.google.com']
# import requests
# print(list(map(requests.get,urls)))

# map can also iterate over dictionaries(dick.keys,values), tuples as well

dict02 = {'a':1, 'b':2, 'c':3}
print(list(map(lambda x: x+7, dict02.values())))

tuple_numbers = (1,2,3,4,5)
print(list(map(lambda x: x+7, tuple_numbers)))

print('')
print('.......................................................functions with multiple arguments.....')
# def add(num1,num2):
#     return num1 + num2
numbers = [1,2,3,4]
numbers2 = numbers.copy()
numbers3 = [10,20,30,40]
print('Multiple_arguments: ', list(map(lambda x,y,z: x+y+z, numbers,numbers2,numbers3)))


print('')
print('........................................................filters......')

"""FILTRY -dwa argumenty 1- funkcja, gdzie wynikiem ma byc tylko true albo false,    2- kolekcje
nie modyfikuje kolekcji, nie przeprowadza zadnychh operacji, zwraca te elementy ktore funkcja okresliła jako True"""
wynik3 = filter(lambda x: x % 2 == 0, liczby)
print("filter: ", list(wynik3))

print('')
print('.....................................................PyMoodra..........filters  in Python.......')
'''filters out elements/events based on boolean conditions'''
def is_even(x):
    if x%2==0:
        return True
    else:
        return False

nums_list = list(range(10))
print(nums_list)
# filter keep only element with true value. when is true it keeps the value when oit is false it discards
# first element of Filter function is FUNCtion, and the second is list

print(list(filter(is_even,nums_list)))

#with lambda function
print(list(filter(lambda x: x%2==0,nums_list)))

# compound functions
print(list(filter(is_even,map(lambda x: x+x,nums_list))))

import requests
urls2 = ['https://www.geeksforgeeks.org', 'https://www.w3schools.com/', 'https://www.google.com', 'https://www.fdgoa.com/']

def get_urls(url):
    try:
        data=requests.get(url,timeout=1)
        return data
    except requests.exceptions.RequestException as e:
        return None

print("def get-urls: ",get_urls(urls2))

print(list(filter(lambda url: get_urls(url) !=None, urls2)))




