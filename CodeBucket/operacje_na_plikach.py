# "r" - Read - domyslna wartosc,otiwera plik do odczytu, zwraca bład gdy plik nie istnije.
# "a" - Append - otiwera plik w trybie dopisywania, tworzy go jesli nie istnieje. tylko dołącza,nie usuwa
# "w' - write - otwiera plik do zapisu, otwiera gojesli nie istnieje, mozna usuwac stare dane, nadpisuje dane
# "x" - create - tworzy okrelsony plil. zwraca bład jesli plik o tej nazwie juz isnieje
# "r+" - read and update - otwiera plik w trybie do odczytu i zapisu, jesli plik nie istnieje zwraca blad.
# "w+" - write and update - otwiera plik w trybie zapisu i odczytu, jesli plik nie istnieje zostanie utworzony.
#
import os

# code_bucket = open("mama.txt", "a")
# global kwoty_przewalut = []
# code_bucket = open("code_Bucket.txt", "a")
# os.remove("mama.txt")

# def na_franki(*kwotyzl, kurs=4.65): # mozemy podac kilka kwot
#     kwoty_przewalut = []
#     for kwota in kwotyzl:
#         suma = round(kwota / kurs, 2)
#         kwoty_przewalut.append(suma)
#     return kwoty_przewalut
#
# kwoty_przewalut = na_franki(100,30,10,15,23,45)
# plik = open("kwoty.txt", "w")
# for kwota in kwoty_przewalut:
#     plik.write(str(kwota) + "\n")
# plik.close()
#
# # # plik = open("kwoty.txt", "a")
# # plik.write(str(na_franki(3.50, 45, 89.34)))
# # plik.write(str(na_franki(3.4)) + "\n")
# # plik.write(str(na_franki(8.5)) + "\n")
# # plik.write(str(na_franki(8.5, 4,80)) + "\n")
#
# na_zloty = open("na_zloty.txt", "w")
# kurs = 4.65
# for i in kwoty_przewalut:
#     i = round(i * 4.65)
#     na_zloty.write(str(i) + "\n")
# na_zloty.close()
#
# for l in range(10,1001,10):
#     code_bucket.write(str(l) + "\n")
# code_bucket.close()
#
# code_bucket = open("code_Bucket.txt", "r")
#
# kwoty = []
#
# for k in code_bucket:
#     kwoty.append(float(k))
#
# dupa = open("dupa.txt", "w")
# for w in kwoty:
#     wynik = round(w / kurs, 3)
#     dupa.write(str(wynik) + "\n")
#
#
#
#
#
