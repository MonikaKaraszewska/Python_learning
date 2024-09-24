l_palindromow = 0
# with poznasz w innej części kursu, więc zostaw suba ;)
with open("yesNo.txt", "r") as wynik:
    for word in wynik:
        if (word.strip() == "tak"):
            l_palindromow += 1

if l_palindromow == 69:
    print("Gratulacje, twój program działa.")
else:
    print("Niestety program nie działa, liczba palindromów się nie zgadza.")