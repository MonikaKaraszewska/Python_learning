lista1=[0,1,2,3,4,"A",5,6,7]
print("lista1", lista1)
lista2=lista1[::-1] #odrócenie elementow w liscie
print(lista2)
print("to samo?: ",lista1[::-1])

# true / false pytamy czy sie znajduje czy nie
lucky = 16
moje = [12,34,56,78,93,23,14,16]
print (lucky in moje)

print(".............................................111.......")

lucky = 16
moje = [12,34,56,78,93,23,14,16]
print (lucky not in moje)

#usun powtarzajace sie liczby
lista3=[0,1,2,3,3,4,"A",5,6,6,7,0,1,2,3,4,"A",5,6,7]
print(lista3.count(6)) #liczymy ile razy pojawiasie element na liscie
print(lista3[6]) # wyswietl element o indeksie '6'
print(len(lista3))
lista3bezpowtorek = []
for l in lista3:
    if l not in lista3bezpowtorek:
        lista3bezpowtorek.append(l)
print(lista3bezpowtorek)

print(".............2...........................222..", "\n")
zbiorSet = {0,1,2,3,4,"A",5,6,7} #zbior=set bez porzadku, nie moznazmieniac, i niema duplikatów
zbior = set()
zbior.add((3))
zbior.add((2))
zbior.add((1))
zbior.add(("tak"))
print(zbior)
zbior.remove(1)
print("zb1", zbior)
print("............3................................333..")
for el in zbior:
    print(el)

#laczenie zbiorow
zbior3 = zbiorSet.union(zbior)
print(zbior3)

#wyswietl elementy wspolne zbiorow

zbior4 = zbior.intersection(zbiorSet)

print(zbior4)
# zbior.clear()
print(zbior)

print("...........................................extend..")

lista1.extend(zbior)
print(lista1)

print("...........................................difference..")

print(zbior)
print(zbiorSet)
zbior4 = zbior.difference(zbiorSet)
print("1", zbior4)
zbior4 = zbiorSet.difference(zbior)
print(zbior4)

lista4 = [0, 1, 2, 3, 4, 5, 6, 7, 'tak', 'A', '0']

print(max(filter(lambda x:  isinstance(x, float) or isinstance(x, int), lista4)))
