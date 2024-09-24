plik = open("test.txt", "a")
print(plik.name)

if plik.writable():
    ileWyrazow = plik.write(input("wprowadz tekst: ") + "\n")
    print("zapisano;",ileWyrazow)
plik.close()

plik = open("test.txt", "r")
if plik.readable():
    print("zawartosc pliku")
    # tresc = plik.read()
    tresc = plik.readlines()
    print(tresc)
    for lit in tresc:
        print("lala:" + lit)
    print ("ilosc slow w pliku:", len(tresc))


# with open('test.txt') as plik:
#     for linia in plik:
#         print(plik.readline())
#     rozmiar = 20
#     tresc = plik.read(rozmiar)
#     while len(tresc)>0:
#         print(tresc)
#         tresc = plik.read(rozmiar)



# print(plik.fileno())
