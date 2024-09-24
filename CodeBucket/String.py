imie = "Joanna"
nazwisko = "Karaszewska"
# print(imie +" " + nazwisko)
# print(imie, nazwisko)
# print(imie *2)
# print(imie, nazwisko, sep="*",end=" to juz jest koniec")
# print ("......................................................................")
# print(imie, nazwisko, "*", " to juz jest koniec")
# print("......................................................................")
# print("Jan \nKowalski")
# print("Jan \tKowalski")
# #
print(".....String a List....................String a List...............................String a List..........")
mojString = "277490118768780291"
print(len("277490109874710980291"))
print(len(mojString))
print(mojString[0]) #wyswietla element o indeksie[0]
print(mojString[0:7])
print(mojString[0:-7])

# # for l in mojString:
# #     print(l)
# print("1" in mojString)
# print(mojString.index("7"))
# print(mojString.count("7"))
#
print(".....................................................fflflf.................")
# zamienc string na liste, czyli rozdzielamy string
# dniTygodnia = "poniedzialek, wtorek, sroda czwartek piatek sobota niedziela"
# dniTygodnia = dniTygodnia.split(" ") # "" w tym podajemy co ma rozdzielac elementy w stringu, i od tego momentu to juz jest lista, nie string
# print(dniTygodnia)
# # łaczyć elementy
# #to juz jest lista
# dniTygodnia = "-".join(dniTygodnia)
# print(dniTygodnia)
print("......................................................................")
#
# imie = input("podaj imie: ")
# print(imie.upper())
# print(imie.capitalize()) #pierwszalitera jest duza
# print(imie.title()) #jak podajemy kilka wyrazow w input on zamienia pierszwe listery na duze,np imiei nazwisko
# print(imie.islower()) #sprawdza czy wpisany imput jest z małych (isupper) duzych lister
#
# zamieniamy string na list metoda list()
# nazw= input("podaj nazwisko")
# nazw = list(nazw)
# print("lista", nazw)
# print("........................................................................endwsith.........")
#
# # mozemy srawdzic najaka litere konczy sie input wpisany przez uzytkownika,np w ten sposob mozemy sprawdzic płec
# if imie.endswith("a"):
#     print("witam Pania")
# else:
#     print("witam Pana")
# #mozemy psrawdzic czy string(input) rozpoczyna sie od znaku,ciagow znakow
# print(imie.startswith("To"))

#replace - zmieniamy podany znak na inny
# nrTelefonu = (input("podaj numer telefonu: "))
# print(nrTelefonu)
# if "-" in nrTelefonu:
#     nrTelefonu = nrTelefonu.replace("-",""), nrTelefonu.replace(" ", "")
# elif " " in nrTelefonu:
#     nrTelefonu = nrTelefonu.replace(" ", "")
# print("ico wyszlo?:", nrTelefonu)



# nrTelefonu = nrTelefonu.strip() # usuwa spacje na poczatkui na koncu stringa
# nrTelefonu = nrTelefonu.lstrip() # usuwa spacje tylkopo lewej
# nrTelefonu = nrTelefonu.rstrip()
# print(nrTelefonu)
# print(nrTelefonu.replace(" ", ""))

# print(".................................................................czy string składa sie z liter alfabetu.....")
# print("abc".isalpha())
# print("sd234".isalpha())
# print(mojString.isalpha())
# print(imie.isalpha())
print("......................................................czy string składa sie z lister i liczb.....")

print("abc".isalnum())
print("sd234".isalnum())
print(mojString.isalnum())
print(imie.isalnum())
#
# print("......................................................czy string składa sie tylko z cyfr.....")
# print("abc".isnumeric())
# print("sd234".isnumeric())
# print(mojString.isnumeric())
# print(imie.isnumeric())
#
# print("......................................................czy string składa sie tylko ze spacji....")
# print(mojString.isspace())
# print("                ".isspace())
# print("       3     ".isspace())



print("..............................................#String formatting............")
name1 = "Tom"
name2 = "Magic"
wiek = 34

print(f"hello there {name2} and {name1}") # to 'f' na poczatku wskazuje na format {} w nawiasach klamrowych wskazujemy jaki ma byc format
print ("Hello zame {} lat {}".format(name1, wiek))
print("witajcie %s and %s" %(name1, wiek)) #%s-string, %f-float, %d-decimal, %r - raw, czyli tak jak wystepuje i dlatego wyswietki sie w cudzysłowiu


#???????????????????????????????
# for l in enumerate(name2):
#     print(l[0] + 1, l[1])

str1 = "PYnative, emma"
str1 = ''.join(reversed(str1))
print("Reversed String is:", str1)

print('.....rindex()	Searches the string for a specified value and returns the last position of where it was found.............')
str2 = "Emma is a data scientist who knows Python. Emma works at google."

print(str2.rindex('Emma'))

print(str2.rfind('Emma'))
print("....")
print(str2.count("m"))