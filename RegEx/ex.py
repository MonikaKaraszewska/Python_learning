import re
input = "Maciej Karaszewski"
pat = "Maciej"

regex = re.match(r'^[A-Z][a-z]+\s[A-Z][a-z]+[^\d]$', input)
print("regex:",regex)

dane = re.match(r'(?P<imie>^[A-Z][a-z]+)\s(?P<nazwisko>[A-Z][a-z]+[^\d]$)', input)
print("Dane: ",dane.group())
print(dane.groupdict())


print(re.search('Macie.',input))

print(re.search('Maciej',input).end())
print(re.search('Karaszewski',input).start())


data = '26-08-2020'
data2 = '26-sier-2020'
datamatch = re.match(r'^[\d]{2}-[\d]{2}-[\d]{4}$', data)
print(datamatch)

datamatch = re.match(r'^[\d]{2}-[\d]{2}-[\d]{4}$', data).end()
print("End: ",datamatch)

datamatch2 = re.match(r'^[\d]{2}-[\w]+-[\d]{4}$', data2)
print(datamatch2.group())


