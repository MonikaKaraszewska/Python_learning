import re
## ma zaczynac sie na wilka litere, a malych moze byc dowolna ilosc
## [a-z]*& ta gwiazdka oznacza ze zakres z ostatniegozbioru moze byc powtorzony nieskonczonailosc
##[a-z]a*& teraz oznaza ze a moze byc powtorzona dowolnie

print('...............................................................***.*&..........')
if re.match("^[A-Z][a-z]*$","A"):
    print("dopasowano")
else:
    print("NIE dopasowano")

print('................................................................++++.&.........')
# plus pozwala na wystapielnie znaku pzy ktorymsie znajduje nieskoczonosc razy, ale pod warunkiem ze chociaz raz ten znak wystapi
# * przy uzyciu gwiazki znak moze sie pojawic ale nie musi

if re.match("^[A-Z][a-z]+$", "A"):
    print("dopasowano")
else:
    print("NIE dopasowano")

print('....................................................?????????..................')
##  ? mowi ze znak moze wystapic maxymalnie jeden raz  ale nie moze nie wysapic w ogole
if re.match("^[A-Z][a-z]?[A-Z]$","AA"):
    print("dopasowano")
else:
    print("NIE dopasowano")

if re.match("^[A-Z][a-z]?[A-Z]$","AllllA"):
    print("dopasowano")
else:
    print("NIE dopasowano")

print('...............................................................{}........')
## {} w nawiazach klamorych deklarujemy minimalna ilosc powtórzen znnaku, a poprzecinku maksymalna wartosc
## czyli ^[A-Z][a-z]{2,5}$" minimalnie 2 duze litery, makzymalnie 5 malych

if re.match("^[A-Z][a-z]{2,5}$","Ala"):
    print("dopasowano")
else:
    print("NIE dopasowano")

##  ^[A-Z][a-z]{2,}$"  jak okreslimy ttylko jedna wartosc to znaczy ze druga jest bez limitu

if re.match("^[A-Z][a-z]{1,}$","A"):
    print("dopasowano")
else:
    print("NIE dopasowano")