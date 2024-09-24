import re
print(".......................convert a date of yyyy-mm-dd format to dd-mm-yyyy format....zamiana miejsc!!!!! ")
dt = '2013-12-17'
print('Data: ', dt)
odp25 = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
print(odp25)


input = "Maciej Karaszewski"
dane = re.match(r'(?P<imie>^[A-Z][a-z]+)\s(?P<nazwisko>[A-Z][a-z]+[^\d]$)', input)
print("Dane: ",dane.group())
zamianaMiejsc = re.sub(r'(^[A-Z][a-z]+) ([A-Z][a-z]+[^\d]$)','\\2 \\1', input)
print("ZamianaMiejsc: ",zamianaMiejsc)
print("")
print('....................................................dalej video_9....?:..')

#?:- no capture group
munst = '1234 578393'
munst45 = re.findall(r"(\d)+",munst)
print(munst45)
munst47 = re.findall(r"((\d)+)",munst)
print("must47: ", munst47)

#
munst46 = re.findall(r"(?:\d)+",munst)#?:wyswieti nam zawartosc grupy,a nie wartosc,czyli tylko4,3
print(munst46)

print(".......................................")
# chcemy wyswietlic imoiona,ktore w id maja 123, ale tylko imiona wyswietlamy
string = '123123123 = Alex, 123123123 = Danny, 123123123  = Mike, 12345 = Ula, 1245 = John'
imiona = re.findall(r'(?:123.*?)+ = (\w+),',string)
print('imiona:',imiona)

print(".......................................")
string3 = '1*1*1*1*2222 1*3333 1*1*5555 2*2*999 5*5898 1*1*909'
string33 = re.findall(r'(?:1\*){2,}\d+',string3)
print("string33: ", string33)

print("...........................?: non-capture - mozna zasotsowac do search i match............")
searchmunst = '1234 57839'
searchmunst1 = re.search(r'(?:\d)+',searchmunst)
print("searchmunst1: ", searchmunst1.group())

#
print("..........................backreferences - using capture gropus inside other operations.............")
# \1 odnosi sie do utworzonej grupy pierwszej, czyli powtorz dokladnie te samagrue

merry = 'Merry Merry Christmas'
merry1 = re.search(r'(\w+) \1', merry)
print("merry1: ", merry1)

happy = 'Happy Happy Holidays. Merry Christmas Christmas '
happy1 = re.findall(r'(\w+) \1', happy)
print("happy1: ", happy1)

christmas = 'Happy Happy Holidays. Merry Christmas Christmas Happy Happy Holidays'
christmas1 = re.findall(r'(\w+) \1', christmas)
print("christmas1: ", christmas1)
