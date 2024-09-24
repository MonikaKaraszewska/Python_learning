import re
string = 'abababababababababa'
wynik = re.search('(ab)+',string) # tu szuka ab, wzoru szuka, grupy szuka, to taki mini pattern
print("wynik:",wynik)


wynik2 = re.search('[ab]+',string) #tu szuka albo b albo a
print("wynik2:",wynik2)

string3 = 'abababbbbabcccc7adccb'
wynik3 = re.search('(ab)+',string3)
print("wynik3:",wynik3)
wynik32 = re.search('[ab]+',string3)
print("wynik32:",wynik32)
wynik33 = re.search(r'[ab]+\w+',string3) # allow flexibility
print("wynik33:",wynik33)

print('')
print("..............Nuances to be wary of..................!!!!!!!")
string4 = 'abababababababababa'
wynik4 = re.search('(ab)+',string4) # tu jest stowrzona jedna grupa
print("wynik4:",wynik4)
print("wynik4.Group: ",wynik4.group(1)) # grupy liczymyod 1. grupa 0, wyswietli wszystkie grupy
# print("wynik4.Group: ",wynik4.group(2)) # nie ma takiej grupy
print('')
string5 = 'abababababababababa'
wynik5 = re.search('(?P<G1>ab)+(?P<G2>ab)+',string5)# sa dwie grupy(ab) pierwsza wezmie ile sie da, i zostawi drugiej minimum
print("wynik5:",wynik5)
print("wynik5Grupy:",wynik5.groups())
print("wynik5Span:",wynik5.span(1))
print("wynik5G1:",wynik5.span("G1"))
print("wynik5G2:",wynik5.span("G2"))

string5 = 'abababababababababa'
wynik5 = re.search('(ab)+(ab)+',string5)
print("wynik5:",wynik5)

liczby = '123456789'
liczwynik = re.search(r"(\d)+", liczby) # jak uzywamy quantifers do grup, wartosc zostaje  aktualizowana az do ostaniej, ktora spelnia wymaganiadlatego otrzymujmey 9
print("liczwynik: ",liczwynik)
print(liczwynik.groups()) # jest tylkojedna grupa i oddaje ostatnia wartosc
print('')
print(".........................quantifiers with groups within findall..............findall......")

liczby2 = '1234 56789'
liczwynik2 = re.findall(r"(\d)+", liczby2)
print("liczwynik2: ",liczwynik2)
liczwynik3 = re.findall(r"((\d)+)", liczby2) #engulf caly pattern w nawiasy engulf = pochłaniac
print("liczwynik3: ",liczwynik3)
print("liczwynik33: ",liczwynik3[0])
print("liczwynik34: ",liczwynik3[1][0])
print('')

string6 = 'abbbbbbb ababababababa'
string6wynik = re.findall('(ab)+',string6) #dostaniemy ostania pare ktora spełnia kryteria last instance
print("string6wynik6: ", string6wynik)
string6wynik7 = re.findall('((ab)+)',string6)
print("string6wynik7: ", string6wynik7)
print(' ')
print(".............................Gropus for word completion.................")


happyB = re.search('Happy (Valentines|Birthday|Anniversary)', "Happy Birthday")
print(happyB)
happyC = re.search('Happy (Valentines|Birthday|Anniversary)', "Happy Valentines")
print(happyC)