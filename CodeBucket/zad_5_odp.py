# 1. Otwieram plik z wyrazami w trybie do odczytu.
wyrazy = open("wyrazy.txt", "r")
# 2. Otwieram plik w którym zapisze wynik, w trybie do zapisu.
wynik = open("prawidlowy_wynik.txt", "w")

# 3. Przechodzę przez kolejne linijki w pliku, czyli przez kolejne wyrazy do sprawdzenia.
for wyraz in wyrazy:
    # 4. Z wyrazu usuwam zbędne spacje (patrz końcówka części o operacjach na stringach).
    wyraz = wyraz.strip()
    # 5. Sprawdzam czy wyraz jest taki sam jak wyraz odwrócony,
    # jako trzecią liczbę w wycinku podałem ujemny przeskok, dzieki temu wyraz zostanie odwrócony.
    if wyraz == wyraz[::-1]:
        # 6. Jeśli prawda zapisuje do pliku "tak" w osobnej linijce.
        wynik.write("tak" + "\n")
    else:
        # 7. Jeśli fałsz zapisuje "nie"
        wynik.write("nie" + "\n")

# 8. Zamykam oba pliki.
wyrazy.close()
wynik.close()

"""
    W celu odwrócenia stringa można też przekonwertować go na listę, 
    a potem go obrócić metodą reverse, ale nie polecam takiej metody, 
    dużo niepotrzebnego zamieszania.
    Jedną linię kodu: 
        if wyraz == wyraz[::-1]
    zastępujemy czteroma, kod staje się mniej czytelny i prosty:
        nieodwrocony_wyraz = wyraz[:]
        wyraz = list(wyraz)
        wyraz.reverse()
        if "".join(wyraz) == nieodwrocony_wyraz
"""