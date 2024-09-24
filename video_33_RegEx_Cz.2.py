import re

if re.match("ko.","kot"):
    print("dopasowano")
else:
    print("NIE dopasowano")

print("..................................................................")
if re.match("ko.","ko9"):
    print("dopasowano")
else:
    print("NIE dopasowano")

print("..................................................................")

if re.match("ko.","kat"):
    print("dopasowano")
else:
    print("NIE dopasowano")

print("..................................................................")
## ^ tak ma sie zaczynac, & a tak konczyc,czyli ko.(i cos) nic wiecej
if re.match("^ko.$","kotttttttt"):
    print("dopasowano")
else:
    print("NIE dopasowano")

print(".........................................................upper lower.........")

#[Kk] oznacza klase znakow, jesli dopasuje chociaz jeden z nich to ok
if re.match("^[Kk]o.$","Kot"):
    print("dopasowano")
else:
    print("NIE dopasowano")

print(".........................................................z duzej litery jakiekolwiek liyery aby byla duza........")
#moze byc tez [B-P]
if re.match("^[A-Z]o.$","Rot"):
    print("dopasowano")
else:
    print("NIE dopasowano")

print("...................................................tylko litery bez innych znakow......")

if re.match("^[A-Za-z]o.$","aot"):
    print("dopasowano")
else:
    print("NIE dopasowano")

print("...................................................wszystko poza tymco jest w nawiasie......")
## ^ ten symbolmusi byc wewnatrz zbioru[^A-Z], wtedy neguje to co jest w zbiorze,czyli nie moze sie zacztnac na lkitere wywar

if re.match("^[^A-Za-z]o.$","bot"):
    print("dopasowano")
else:
    print("NIE dopasowano")

print("......................................................................")

if re.match("^[rR]ok[-_=][0-9][0-9][0-9][0-9]$","Rok-2008"):
    print("dopasowano")
else:
    print("NIE dopasowano")
