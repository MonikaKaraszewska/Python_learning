import re
##(?P<first>ll) gupa indeksowana
##((?:He) grupa bez nazwy bez indeksu


wynik = re.match(r"^((?:He)(?P<first>ll)o)( World)+(!|.)$", "Hello World World!")

if wynik:
    print("dopasowano")
    print(wynik.group())
    print(wynik.group(0))
    print(wynik.group(1))
    print(wynik.groups(3))
    print(wynik.group("first"))


else:
    print("NIE dopasowano")

print(".................................................walidacja adresu email.....................")

if re.match(r"^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9\.-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9-\.])+\.[A-Za-z0-9]$", "9-6monikaa.pl@onet.pl6"):
    print(" dopasowano")
else:
    print("NIE dopasowano")


