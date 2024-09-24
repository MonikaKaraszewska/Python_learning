import time


tekstUsera = input("wklej dlugi tekst: ")
start_time = time.time()

ileZnakow = len(tekstUsera)
print("\n", "Wszystkich znakow jest: ", ileZnakow)

print("..................LITERY.................")

alfabet = "abcdefghijklmnopqrstuwvxyz"
for l in alfabet:
    il = tekstUsera.count(l)
    print(l.upper() + "->", + il)

print("..................CYFRY.................")
cyfry = "1234567890"
for c in cyfry:
    cl = tekstUsera.count(c)
    print(c + ":",cl)
print("--- %s seconds ---" % (time.time() - start_time))