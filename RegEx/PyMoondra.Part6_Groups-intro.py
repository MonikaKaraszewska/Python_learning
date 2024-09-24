import re
zdanie = "John has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fishes"

zbior01 = re.findall(r"[A-Za-z]+ \w+ \d+ \w+", zdanie)
print("zbior01: ", zbior01)

##() tworzymy grupy jeseli jest choc jedna dupa utworzona to findall wyswietli tylko te grupe ignorujac reszte
# findall nie ma grup no group function, czyli nie ma takjak w match re.match().group
grupa02 = re.findall(r"([A-Za-z]+) \w+ \d+ \w+", zdanie)
print("grupa02: ", grupa02)

grupa03 = re.findall(r"([A-Za-z]+) \w+ \d+ (\w+)", zdanie)
print("grupa03: ", grupa03)

grupa04 = re.findall(r"[A-Za-z]+ \w+ \d+ (\w+)", zdanie)
print("grupa04: ", grupa04)

info = re.findall(r"([A-Za-z]+) \w+ (\d+) (\w+)", zdanie)
print("INFO: ", info)

print("...////////////////////////////////////////////////////////////////////////////////////////////////////////////")

print(".........................zip i gwiazdka............................*zip organize data by categories")
zipoanie = zip(*info)
print(list(zipoanie))

print("...////////////////////////////////////////////////////////////////////////////////////////////////////////////")

infoSearch = re.search(r"([A-Za-z]+) \w+ (\d+) (\w+)", zdanie)
print(".....................................................................................search")
print("INFosearch: ", infoSearch)
print(infoSearch.groups(0))
print(infoSearch.group(0,2))
print(infoSearch.group(3))
print(infoSearch.group(3,2,1,0))

print("................................pokazuje index poczatku i konca................span span ..start/end.............SPAN")
zdanie = "John has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fishes"

print(infoSearch.span())
print(infoSearch.span(3))
print(infoSearch.start(3))

data = re.findall(r"([A-Za-z]+) \w+ (\d+) (\w+)", zdanie) # wyzwietla grupy, grupa po  grupie
print("DATA: ", data)
print(data[2])
# zeby wyswietlic w całosci cosie sparowalo, niepodzielone na grupy
datacale = re.findall(r"(([A-Za-z]+) \w+ (\d+) (\w+))", zdanie)
print("DATAcale: ", datacale)

for i in datacale:
    print("i: ",i[0])

it = re.finditer(r"([A-Za-z]+) \w+ (\d+) (\w+)", zdanie)
# x = next(it).group()
# print(x)
# x = next(it).group()
# print(x)
# x = next(it).group()
# print(x)
# # x = next(it).group()
# # print(x)

for element in it:
    print("element:",element.group(1,3, 2))

# for element in it:
#     print("groups:", element.groups())