from random import randint
# for i in range (100):
#     print(randint(1,10))

los = randint(1,10)
odp = 0
i = 0
print("Zgadnij liczbę przedziału od 1 do 10")

while odp != los:
    i += 1
    odp = int(input("Podaj Liczbę: "))
    if odp > los:
        print ("za duza")
    elif odp < los:
        print ("za mala")
    else:
        print ("Brawo! odgadles za", i, "razem.")