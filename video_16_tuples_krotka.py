#tuple/krotka jest w nawiasach okrągłych (), a nie w kwadratowych jak lista []
#nie mozna zmieniac ich elementów
#
tuple1 = (2, 3, 4, 16, 32, 64, 128,2)
print(tuple1[0])
print(tuple1[6])
print(tuple1)

print("elementow", tuple1.count(4))
print("index", tuple1.index((64)))

print("\nWycinki:")
print(tuple1)
print("A:",tuple1[0:3])
print("B:",tuple1[3:6])

# liczenie do konca, ale zaczynamy liczyc od indeksu 1 nie 0
print("C:",tuple1[-4:-2])

# paramter skoku - pokazuje co 3 liczbe
print("D:",tuple1[1::3])

# od 3indeksu do konca
print("E:",tuple1[3:])

# do 4 indeksu
print("F:",tuple1[:4])

#odwrotne sortowanie
print("G:",tuple1[:4:-1])
print("H:", tuple1[::-1])

# # jak zmienic tuple na liste zeby mozna było ja modyfikowac
# #to ponizej to ciwczenia do Listy nie do krotki

# krotkalist = list(tuple1)
# print(krotkalist)
# krotkalist[2] = "mapa"
# print(krotkalist)
# print(krotkalist + ["sok"])
# print(krotkalist)
# krotkalist += "dupapapa"
# krotkalist += ["dupapapa"]
# print(krotkalist)



print("......................dzieleinie krotki")
a,b = tuple1[:3], tuple1[3:]

print(a)
print(b)



# krotka = (1, 2, 3, 4, 5, 6, 7, 8)
# indeks_podzialu = 3
#
# czesc_pierwsza, *czesc_druga = krotka[:indeks_podzialu], *krotka[indeks_podzialu:]
#
# print("Część pierwsza:", czesc_pierwsza)
# print("Część druga:", czesc_druga)