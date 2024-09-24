import re
# \w 	Returns a match where the string contains any word characters
# (characters from a to Z, digits from 0-9, and the underscore _ character)
names = [ "Finn Bindeballe",
          "Geir Anders Berg",
          "HappyCodingRobot",
          "Ron Comberg",
          "Sohil"
          "Ala",
          "Ogon58",
          "Monika      Karaszewska"]

print("..................................find people with the first and last name only......")
# \s+ nie wazne ile jest sapcji pomiedzy
regex = r"^\w+\s+\w+$"
print('regex: ', regex)
for name in names:
    result = re.search(regex,name)
    if result:
        print(result)

print("..................................search for word char sequence starting with C......")

regex = r"C\w*"

for name in names:
    match = re.search(regex,name)
    if match:
        print(name)
        # print(match.start())
        # print(match.end())
        print((match.span()))
        print(match.group())
print("......................................")

imiona = [ "Finn Bindeballe",
          "Geir And!ers Berg",
          "HappyCodingRobot",
          "Ron Comberg",
          "Sohil",
          "Patric German",
          "Ogon58",
          "Monika      Karaszewska"]

regex2 = r"^\w+\s+\w+$"

for imie in imiona:
    para = re.search(regex2,imie)
    if para:
        print(imie)

print("..................grupy - jednaimie, druga nazwisko....................")

regex3 = r"^(\w+)\s+(\w+)$"

for imie in imiona:
    para = re.search(regex3,imie)
    if para:
        # print(imie)
        print(para.group(1))
        print(para.group(2))

print("..................grupy - jednaimie, druga nazwisko.....................z nazwami grup...............")

regex4 = r"^(?P<fn>\w+)\s+(?P<ln>\w+)$"

for imie in imiona:
    para = re.search(regex4,imie)
    if para:
        # print(imie)
        print(para.group('fn'))
        print(para.group('ln'))

print("..................detect extra charachtersliek &%#!.............")

imiona2 = [ "Finn Bindeballe",
          "G!eir Anders Berg",
          "HappyCodingRobot",
          "Ron Comberg",
          "Sohil",
          "Patric German",
          "Ogon58",
          "M!onika      Karaszewska",
            "m!sha"]

regex5 = r"^[A-Za-z!]+\s+[A-Za-z]+$"

for imie in imiona2:
    if re.search(regex5, imie):
        print(imie)


print("..................detect extra charachtersliek &%#!.............")
regex6 = "[a-z]+"
for name in imiona2:
    pary = re.findall(regex6,name)
    if pary:
        print(pary)

print("..........................................match /  fullmatch..............")

adresy = ["https://www.helion.pl",
         "http://helion.org/",
         "hfile://helion.pl",
         "com.helion.pl/"]

regex7 = "https?"
for adres in adresy:
    if re.match(regex7,adres):
        print(adres)

regex8 = r"https?://.\w+.(org|pl)/"
for adres in adresy:
    if re.fullmatch(regex8,adres):
        print("fullmatch: ",adres)