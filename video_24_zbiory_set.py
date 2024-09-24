#zbior
# w zbiorze nie ma ineksów, niemozna odwołc sie do elementu przez indeks
liczby1 = {0, 1, 2, 4}
# zaiana listy na set
slowa1 = [3, 4, 5, 6, 7]
slowa1 = set(slowa1)
print(slowa1)

slowa = set({"a", "b", "c", "c"})
print(slowa)

# dodawanie elementu dozbioru
liczby1.add(5)
print(liczby1)

#usuwanie czegosc
liczby1.remove(0)
print(liczby1)

# Set - wartosci sie nie powtarzaja, nie moze byc dwoch piatek,
liczby1.add(5)
print(liczby1)

# czy w zbiorze znajduje sie 1
print(1 in liczby1)
print("a" in liczby1)

#operacjena zbiorach
liczby1 = {0, 1, 2, 4,7}
liczby2 = {9,1, 8, 7, 6, 4}

print("liczby1: ", liczby1)
print("liczby2: ", liczby2)


print(liczby2 | liczby1) # | - to jest suma // wynikiem jest połaczenie zbiorow, bez powtarzajacych sie elementow bo w zbiorach elemenyty sie nie moga powtarzac!!
# print(liczby1 | slowa)


# '&' czesc wspolna zbiorów
print(liczby2 & liczby1)

# "-' minus - operatora różnicy (-) do uzyskania różnicy między nimi.
# Różnica dwóch zbiorów zwraca nowy zbiór, który zawiera elementy obecne tylko w jednym ze zbiorów.
print("minus-róznica: ", liczby2 - liczby1) # wazna jest kolejnosc zbiorów
print("minus-róznica: ", liczby1 - liczby2)


# '^' - róznica symetryczna, czyli otrzymujemy zbiór róznic,Różnica symetryczna zwraca zbiór elementów,
# które są obecne w jednym z zbiorów, ale nie w obu jednocześnie.
print("roznica Symetryczna: ",liczby2 ^ liczby1)


liczby1.update({99,44,33,4})
print(liczby1)

