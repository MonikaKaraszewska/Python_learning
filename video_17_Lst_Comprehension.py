lista = list(range(10))

print(lista)

nowa = [i * 2 for i in lista] #wez liste i kazdy argument potraktuj jako zmienna 'i', i na tej zmiennej 'i'
# kazdy ten argument pomnóz przez2, i zwróc nowa liste po modyfikacjach
print(lista)
print("Nowa lista:", nowa)

nowa2 = [i + 1 for i in lista if i % 2==1] #najpierw sprawdzany jest warunek 'if i % 2==1' a potem dodawane jest "i + 1 '
print(nowa2)

#Formatowanie String

argumenty = ["Monika", 41]
tekst = "hej, mam na imię {0} i mam {1} lat.".format(argumenty[0], argumenty[1])
print(tekst)

print("inny sposob: ")
argumenty = ["Monika", 41]
tekst = "hej, mam na imię {imie} i mam {wiek} lat.".format(imie = argumenty[0], wiek =  argumenty[1])
print(tekst)

print('...............Python Simplified ....................')

fruits = ['apples', 'bananas', 'strawberries']

[print([i.upper() for i in fruits])]
upperfruit = [i.upper() for i in fruits]
print(upperfruit)
print([i.upper() for i in fruits])
print('')

bits = [False, True, False, True, False, True, False, True, False, True, False, True,]

print([1 if b == True else 0 for b in bits ])

print(' .............................string manipulation..')

my_string = "HelloMyNameIsMonika"
my_string1 = ''.join([i if i.islower() else ' ' + i for i in my_string])
print(my_string1)
my_string = ''.join([i if i.islower() else ' ' + i for i in my_string])[1:] # to na koncu usunelo spacje z pocztaku zdania
# bowstawiamy spacje przed wielkimiliterami, no i w efekcie przed pierwsza mamy spacje
print(my_string)

my_string2 = ''.join([i if i.islower() else ' ' + i.lower() if i in ["N", "I"] else ' ' + i for i in my_string])[1:]
print(my_string2)

my_string3 = ''.join([i if i.islower() else ' ' + 'BANANANA' if i in ["N", "I"] else ' ' + i for i in my_string])[1:]
print(my_string3)