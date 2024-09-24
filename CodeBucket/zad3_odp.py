import time

zdanie = input("wprowadz tekst: ")
start_time = time.time()

zdanie = zdanie.lower()
zdanie = list(zdanie)
#print(zdanie)
#zdanie.sort()
litery = {} #słownik, gdzie kluczmi sa litery a ilosc ich wartosciami
alfabet = "abcdefghijklmnoqprstuwvxyz"
for l in alfabet:
     litery[l] = 0
for znak in zdanie:
    #if znak.isalpha():
    if znak in alfabet:
        litery[znak] = litery[znak] + 1

for znak, ilosc in litery.items():
    print(znak, "->", ilosc)
#print(litery)
print("--- %s seconds ---" % (time.time() - start_time))