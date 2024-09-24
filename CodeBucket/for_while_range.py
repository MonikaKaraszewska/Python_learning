print (".................................podaj haslo")
# haslo = input("podaj Haslo: ")
#
# # teraz po podaniu niepoprawnego hasla program konczy
# if haslo == '1234':
#     print("jstes w sysemie")
# else:
#     print("haslow błedne")


print (".................................podaj haslo.....................Break")

# poprzez petle while bedzie pytal o haslo az podamy poprawne
'''while True: # while True - wykonuj sie cały czas 
    haslo = input("podaj Haslo: ")
    if haslo == '1234':
        print("jestes w systemie")
        break; # zakonczy jak podam wlasciwie haslo
    else:
        print("haslow błedne")'''


print (".................................podaj haslo.....................continue ...........")

# chcemy wpisac i, od 0-20 poza wielokrotnociami 3
i = 0
while i < 20:
    i += 1
    if i % 3 == 0:
        continue # czyli omin to co jest w if wyzej
    print(i)





'''print (".................................AAAAAAAAAAAAAAAAAAAAAAA")
i=0
while i < 10: #dopóki i jest mniejsze od 10 to:
    print(i) # wydrukuj
    i+=1 # dodaj 1 i z ta wartoscia zacznij petleod nowa'''


'''print (".................................BBBBBBBBB")
print(6789//10)
lista = []
n = int(6789)
while n > 0.5:
        lista.append(n%10)
        n = n//10
print(lista)'''

print (".................................cccccccccccccccc")
''''
n=1
while n<10:
    n *= 2
    print(n)

print (".........................NOWE")

for i in range(10):
    if i == 6:
        print(i)
        break
print (".....porownaj z wyzej....................NOWE")
for i in range(10):
    if i == 6:
        break
    print(i)

print (".........................NOWE")
for i in range(2,10):
    if i == 6:
        continue
    print(i)

print ("......................................................range")

# w zakresie od 0-50 ywsiwetlaj co 3 liczbe
for z in range(0,50,3):
    print(z)'''


