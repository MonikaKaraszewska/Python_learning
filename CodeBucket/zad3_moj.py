import time


tekstUsera = input("wklej dlugi tekst: ")
start_time = time.time()

ileZnakow = len(tekstUsera)
print("\n", "Wszystkich znakow jest: ", ileZnakow)

alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","r", "s", "t", 'u', "w", "v", "x", "y", "z"]
for lit in alfabet:
    lit2 = tekstUsera.count(lit)
    print("{0} - {1}".format(lit.upper(), lit2))

print(".......Cyfry.......................")
cyfry = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
for c in cyfry:
    c2 = tekstUsera.count(c)
    print("{0} - {1}".format(c.upper(), c2))




print("--- %s seconds ---" % (time.time() - start_time))