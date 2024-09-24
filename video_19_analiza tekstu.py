file = open("text_19.txt", "r")
tekst = file.read()
file.close()

def policz (txt, znak):
    licznik = 0
    for z in txt:
        if z == znak:
            licznik +=1
    return licznik
print(policz(tekst, "a"))
print(policz(tekst, "a") + policz(tekst, "A"))
print(policz(tekst.lower(), "a"))

for z in "abcdefghijklmnoprstuwxyz":
    ile = policz(tekst.lower(), z)
    procent = 100 * ile/ len(tekst)
    # procent = 100 * policz(tekst.lower(), z) / len(tekst)
    print ("{0} - {1} - {2}".format(z.upper(), ile, round(procent,2)))