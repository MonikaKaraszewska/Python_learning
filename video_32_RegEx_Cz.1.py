import re

wzor = r"banan"

tekst = r"gruszkabananjagod\nabananjabłko"
print("tekst:", tekst)

print(re.match(wzor,tekst))

if re.match(r".*" + wzor + ".*",tekst):
    print("dopasowano")
else:
    print("NIE dopasowano")


if re.search(wzor,tekst):
    print("dopasowano search")
else:
    print("NIE dopasowano search")

print(re.findall(wzor,tekst))

dopasowanie = re.search(wzor,tekst)
if dopasowanie:
    print("Gropy: ",dopasowanie.group())
    print(dopasowanie.start())
    print(dopasowanie.end())
    print("SPam:", dopasowanie.span())

 #sub sluzy do zamiany,podmienia
tekst2 = re.sub(wzor,"kiwi", tekst)
print(tekst2)