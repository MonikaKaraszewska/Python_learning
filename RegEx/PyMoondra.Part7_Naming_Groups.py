import re

string = "New York, New York 11369"

stringmatch = re.search(r"([A-Za-z\s]+), ([A-Za-z\s]+)(\d+)",string)
print(stringmatch)
print(stringmatch.group(1))
print(stringmatch.group(2))
print(stringmatch.group(3))
print(stringmatch.group(0))

# ?P<> ?P<postcode>
#re.compile is to save your pattern
wzor = re.compile(r"(?P<City>[A-Za-z\s]+),(?P<State>[A-Za-z\s]+)(?P<ZipCode>\d+)")
stringmatch2 = re.search(wzor,string)
print("stringmatch2: ",stringmatch2)
print("City group: ", stringmatch2.group('City'))
print("State group: ", stringmatch2.group('State'))
print("ZipCode group: ", stringmatch2.group('ZipCode'))


# a kiedy nie wiesz albo zapomniałas jakie grupy sa utworzone
print(stringmatch2.groupdict())

dane = stringmatch2.groupdict()
print(dane.keys())