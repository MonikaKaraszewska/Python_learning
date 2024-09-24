#krotka = tuples - nie mozna ich modyfikowac / /
krotka = (1,2,3, "tak")
print(krotka[0])# mozna spr jaki element znajduje sie na podanym ideksie
print(1 in krotka) # czy element znajduje sie w krotce
print(1 not in krotka)
print(krotka.count(3)) #ile razy wystepuje element
print("wycinki", krotka[1:-1]) #mozna robic wycinki

#mozemy iterowac petla for
for el in krotka:
    print(el *2 *3)

print("......................................................................slownik")
# SLOWNIK - przechowuje dane klucz:wartosc

dicki = {"Asia": "asia@gmail.com",
         "Madzia": "magda@gmail.com",
         "Pawcio": "pawel@gmail.com"}
print(dicki["Asia"]) # wysiwetlac wartosc po kluczu

dicki["Asia"] = "asienka@gmail.com" #mozemy zmieniac wartosci
print(dicki)

# Mozemy przechodzic pętla FOR,ale musimy okreslic czy przechpdzimy przec klucze(dicki.keys, czy wartosci dicki.values

# for klucz in dicki.keys():
#     print(klucz)

for klucz in dicki.keys():
    print(dicki[klucz]) #[klucz] - to oznacza ze wyswietka wartosc po kluczu

print("...........................................................................klucz...............")

for values in dicki.values():
        print(values)
# metoda.items - przechodzimy po kluczch i wartosciach
for klucz, wartosc in dicki.items():
        print("klucz+wartosc: ", klucz + ": " + wartosc)

for wartosc in dicki.items():
        print(wartosc)

print("......................................................................")
print(dicki.get("tomek")) # jak nie ma, to dostajemy NONE, wnawaisie wpisujemy Key (3) albo("tak")
# print(dicki["tomek"]) # jak nie ma,to dostajemy ERROR - KeyError

print(dicki.pop("Asia")) #usuwanie elementów
print(dicki)

print("..................................................................dodajemy....")

#dodajemy, elementy doslownika
dicki["joanna"] = "joasia@gmail.com"
print(dicki)

dicki.update({"Magic": "magic@gmail.com"}) #klamrowe nawiasy,bo tworzmy nowy słownik i dodajemy do poprzedniego
print(dicki)

#dicki.clear() #usuwanie słownika
#print(dicki)
print("............................................................888..........")
print("Joanna" in dicki)

# moje pomysły
for k in dicki.keys():
    k = k.upper()
    print("JOANNA" in k)

print("......................................................................")
print("magda" in dicki) # domyslnie szuka po kluczach
print("Magda" in dicki)
print("magda@gmail.com" in dicki.values())

print(".......................................................fromkeys()...............")

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)