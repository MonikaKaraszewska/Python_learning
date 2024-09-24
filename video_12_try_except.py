# x = 7
# y = 0
#
# try:
#     lista = [3]
#     print(lista[0])
#     print(x + y)
#     print(x / y)
#     print ("linijka po")
# except (ZeroDivisionError, TypeError):
#     print("cos nie tak, sprawdz wprowadzone dane")
# except Exception as e:
#     print("blad dzielenia exc", e)
# # except:
# #     print("innny blad")
# else:
#     print("else")
# finally:
#     print("finally: zawsze sie pokaze!")
#
#
# print("dalsze instrukcje.....")
#
# plik = None
# try:
#     plik = open("plik.txt", "r")
#     for ch in plik:
#         print(ch/2)
# except Exception as e:
#     print("wystapil blad", e)
# finally:
#     if plik:
#         plik.close()


print(".............................Tech with Tim...........")

'''Blok try zawiera kod, który może generować błędy.
Bloki except zawierają kod obsługi błędów. Każdy blok except obsługuje określony rodzaj błędu (typ wyjątku).
Blok else jest opcjonalny i wykonuje się tylko wtedy, gdy nie było błędów w bloku try.
Blok finally jest opcjonalny i zawsze wykonuje się, niezależnie od tego, czy wystąpił błąd, czy nie. 
Jest używany do zasobów zwalnianych, niezależnie od sytuacji.'''


text =input("username:")

try:
    number = int(text)
    print(number)
except:
    print("invalid username")


try:
    x = int(input("Podaj liczbę: "))
    result = 10 / x
    print("Wynik:", result)
except ValueError:
    print("To nie jest liczba całkowita.")
except ZeroDivisionError:
    print("Dzielenie przez zero!")
else:
    print("Nie było błędów.")
finally:
    print("To wykonuje się zawsze.")
