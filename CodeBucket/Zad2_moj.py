iloscOcen = int(input("Podaj z ilu ocen chcesz obliczyc srednia:"))
total = 0

for o in range(iloscOcen):
    m = int(input("podaj ocene :"))
    # total += m
    # if m >= 7:
    #     total -= m
    #     iloscOcen -= 1
    #     print("Wprowadziles nieprawidlowa ocena, ktora nie zostanie wliczona do sredniej")
    while m > 6:
        print("Wprowadziles nieprawidlowa ocena, podaj jeszcze raz")
        m = int(input("podaj ocene :"))
    total += m
    print(total)
srocen = total / iloscOcen

print("podałes", iloscOcen, "poprawne oceny")
print("Twoja Srednia ocen to: ", srocen)

if srocen >= float(4.75):
    print("BRAWO!!!Masz pasek na swiadectwie")
else:
    print("No i, pasek bedzie na dupie!!!!!!!!!!!")






