lista = ["subskrybuj", "kanal", "o", "wszystkim",]
print(len(lista))

# i=0
# while i< len(lista):
#     print(lista[i])
#     i+=1

for x in lista:
    print(x)

print(list(range(10)))

for y in range(1, 11,):
    print(y)
print(list(range(y)))

print("...............................................suma dwoch liczb...zadanie z analityk.edu.pl")

suma = 0
for i in range(11):
    for l in range(i):
        suma = i + l
        if suma == 7:
            print(i, l,suma)

print("...............................................inne zadani")

suma = 0
for i in range(11):
    if i % 2 == 0:
        suma = i + 1
        print(suma)

print("...............................................kolejne zadani")

lata = int(input())
oprocent = float(input())
kapital= int(input())

for i in range(lata +1):
    kapital = kapital + kapital * oprocent
print(kapital)

