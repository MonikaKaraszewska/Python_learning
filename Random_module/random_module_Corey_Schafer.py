import random
import re
import string

# wysweitla od 0-1 bez 0  i 1
value = random.random()
print("value: ",value)
# random float values
value1 = random.uniform(1,10)
print(value1)

# liczby calkowiete
value2 = random.randint(1,6)
print(value2)

#random.choices = losuje z podanej listy
greeting = ['Hello', 'Hi', 'hey', 'cheers', 'hola', 'czesc']
value3 = random.choice(greeting)
print(value3 + ' ', 'monika')

print('')
kolory = ['Red', 'balc', 'green', 'pink']
res = random.choices(kolory,k=10)
print("Res: ", res)

deck= list(range(1,53))
print(deck)
random.shuffle(deck)
print(deck)

hand = random.sample(deck,k=5)
print(hand)

print('')

print(".....................fake data............")

import regex

imionaMeskie = '''
    Antoni - 3862 (lider również w połowie 2020 r.)
    Jan - 3535 (również 2. miejsce)
    Aleksander - 3353 (awans z 4. miejsca)
    Franciszek - 3252 (awans z 5.)
    Jakub – 3236 (3. w 2020 r.)
    Szymon – 2575 (bez zmian)
    Mikołaj – 2536 (awans z 8. pozycji)
    Leon – 2479 (awans z 11. miejsca)
    Filip – 2372 (7. w 2020 r.)
    Stanisław – 2295 (9. w 2020 r.)
'''
imionaMeskie = re.findall('[A-Z][a-z]+',imionaMeskie)
print(imionaMeskie)
nazwiska = '''NOWAK 	100617
KOWALSKI 	68061
WIŚNIEWSKI 	54170
WÓJCIK 	48786
KOWALCZYK 	47992
KAMIŃSKI 	46735
LEWANDOWSKI 	45363
ZIELIŃSKI 	44713
SZYMAŃSKI 	43499
WOŹNIAK 	43487
DĄBROWSKI 	42454
KOZŁOWSKI 	37068
MAZUR 	34063
JANKOWSKI 	33866
KWIATKOWSKI '''
nazwiska = re.findall('[A-ZÓŚĘĄŻŹŃŁ]+',nazwiska)
print(nazwiska)
phone = f'{random.randint(100,999)}-555-{random.randint(1000,9999)}'
print(phone)

lista=[]

for i in range(5):
    fake = f'{random.choice(imionaMeskie)} {random.choice(nazwiska)} nr telefonu {phone}'
    lista.append(fake)
print(lista)

# dane = {key[enumerate(len(lista))]: v for v in lista}
dane = {key:[val] for (key,val) in enumerate(lista)}
print(dane)
print('')


import string
lista5 = string.ascii_uppercase
dane3 = {key:[val] for (key,val) in enumerate(lista5)}
print(dane3)

