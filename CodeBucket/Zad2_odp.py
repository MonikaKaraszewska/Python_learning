iloscOcen = int(input("Podaj z ilu ocen chcesz obliczyc srednia:"))
oceny = []
total = 0

for m in range(iloscOcen):
    ocena = int(input("podaj ocene :"))
    oceny.append(ocena)
    total += m
srocen = total
print("Z podanych ocen:" +str(oceny))
print("Twoja Srednia ocen to: ", srocen)

if srocen >= 4.75:
    print("BRAWO!!!Masz pasek na swiadectwie")
else:
    print("No i, pasek bedzie na dupie!!!!!!!!!!!")






