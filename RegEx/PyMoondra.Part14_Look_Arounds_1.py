'''4 types of look arounds:
Positive look ahead ?=
Negative look ahead ?! - w tym przypadku potwierdzamy ze ta grupa znakow nie jest za głownym wzorem, confirm that this group does't followw the main pattern
Positive look behind ?<=
Negative look behind ?<!

NIE mylic z:
?: non capture groups
?P<> naming groups
'''

import re
string = ('''ABC1   1.1.1.1     20151118    active
            ABC2    2.2.2.2.    20151118    inactive
            ABC3    x.x.x.x     xxxxxxxx    active''')

patter = re.compile(r'ABC\w\s+(\S+)\s+\S+\s+(?=active)') # szuka tego slowa active,ale nie wyswietla
print("positive_Look_Around: ", re.findall(patter,string))
## niema ABC bo tylko (\S+) to jest w grupie i tylko to wyswietli!!!


patter2 = re.compile(r'ABC\w\s+(\S+)\s+\S+\s+(?:active)')
print("Non_catupring_Group: ", re.findall(patter2,string))

print("positive_Look_Around with search: ", re.search(patter,string)) # nie wyswietla tego active, pomimo ze w grupie sie znajduje
print("Non_capturing_Group with search: ", re.search(patter2,string)) # a tu wyswietli


print('')
print(' ..................difference between non-capture groups and look arounds............')

string2 = 'abababacb'
wzor = re.compile('(?:b)(a)(?:b)')  # spodziewlismy sie 2 'a' ale jest jedno, bo non-capture group consume characters,
print(re.findall(wzor,string2))
wzor2 = re.compile('(?<=b)(a)(?=b)') # nie zjada, doesn't consume tulko sie rozglada i sprawdza
print(re.findall(wzor2,string2))

print('')
print(' .............................................capture the entire look around................')
string2 = 'abababacb'
wzor3 = re.compile('(?=(bab))')
print(re.findall(wzor3,string2))

string4 = 'I love cherries, apples, and strawberries.'
wzor4 = re.compile(r'(\w+)(?=\.|,)')
print(re.findall(wzor4,string4))