# print("Berechnung des größten gemeinsamen Teilers")
# print("mit einem rekursiven euklidischen Algorithmus")
# print("=============================================")
# print(" ")
# # Eingabe
# print("Eingabe der Startwerte:")
# print("-----------------------")
# zahl_1 = int(input("erste ganze Zahl: "))
# zahl_2 = int(input("zweite ganze Zahl: "))
# # Rekursion als Funktion
# def euklid_rek(wert_1,wert_2):
#     if wert_2 == 0:
#         return wert_1
#     else:
#         print("rekursiver Aufruf mit:",str(wert_1),str(wert_2))
#     return euklid_rek(wert_2,(wert_1 % wert_2))
# # Funktionsaufruf und Ausgabe
# print(" ")
# print("Ergebnis:")
# print("---------")
# print("Der größte gemeinsame Teiler ist " + str(euklid_rek(zahl_1,zahl_2)))


print(".......................................euklid2")

print("Berechnung des größten gemeinsamen Teilers")
print("mit einem iterativen euklidischen Algorithmus")
print("=============================================")
print(" ")
# Eingabe
print("Eingabe der Startwerte:")
print("-----------------------")
zahl_1 = int(input("erste ganze Zahl: "))
zahl_2 = int(input("zweite ganze Zahl: "))
# Iteration als Funktion
def euklid_it(wert_1,wert_2):
    while wert_2 != 0:
        print("Schleifendurchlauf mit:",str(wert_1),str(wert_2))
        hilfswert = wert_1 % wert_2
        wert_1 = wert_2
        wert_2 = hilfswert
    return wert_1
# Funktionsaufruf und Ausgabe
print(" ")
print("Ergebnis:")
print("---------")
print("Der größte gemeinsame Teiler ist " + str(euklid_it(zahl_1,zahl_2)))