def args(*args): # nie wiemy jeszcze ile argumentow potrzeba moze ty byc nazwane *kids, i to jest jako krotka,tuples
    suma = 0
    for liczba in args:
        suma+= liczba
    print( suma)

args(3,2,2,1,2) # wywołujmy fukcje, bez print, poprotu nazwa funkcji i play


def wyswietl_dane (imie, rok_ur):
    print (imie)
    print(2023 - rok_ur)

wyswietl_dane("monika", 1982)

def kwargs(** czlonkowie): # dwie ** tworza kwargs i jest to jest odpowiednikiem slownika
    for typ, imie in czlonkowie.items():
        print(typ, "-", imie)
kwargs(mama="zosia", tata="tadzik", brat="jarek")

def przywitanie(imie = "Jan"):
    print("czesc", imie)
przywitanie()

def wyswietl_sume(liczby):
    suma=0
    for liczba in liczby:
        suma+=liczba
    return suma/2


print(wyswietl_sume([2,3,2,2]))



