import re
'''Negative look ahead   ?!
    Negative look  behind ?<! 
    
    negative look ahead / behind sprawdza czy podany wzor NIe jest  w zawarty w naszym output'''

string =""" 
Remaining party applicants:

Occupation: Party PLanner
Occupation: Baking
Occupation: Cook
Occupation: Publicist
Occupation: Entertainer
Occupation: Baker
Occupation: baker
Occupation: pierrot """

pattern = re.compile('Occupation: (?!Baker|Baking|Cook).+', flags=re.IGNORECASE)

print(re.findall(pattern,string))

string2 = '''
Full invitation list:
Guest: Ashley Jackson
Guest: Maria Jackson
Guest: Bill Smith
Entertainer: Michael Johnson
Baker: Chris Jackson
Party Planner: Seema Patel
Publicist: Seema Patel
Baker: Ashley Sanders
'''

pattern2 = re.compile(r'(?<!Baker: )\b\w+\s\w+$',flags=re.IGNORECASE|re.M)
print(re.findall(pattern2,string2))
#dlatego trzeaba uzyc \bword boundaries, bo to sprawdza czy wczesniej jest spacja, albo

pattern3= re.compile(r'(?<!Baker: )\w+\s\w+',flags=re.IGNORECASE|re.M)
print('Pattern3: ', re.findall(pattern3,string2))

# $ sprawdza czy to jest koniec stringu, musimy tez dodac re.MULTILINE czyli re.M zeby sprawdzal kazda linijkę
pattern4 = re.compile(r'(?<!Baker: )\b\w+\s\w+$',flags=re.IGNORECASE|re.M)
print('Pattern4: ',re.findall(pattern4,string2))

print(' ')
string3 = '''
Full invitation list:
Guest: Ashley Jackson
Guest: Maria Maria Jackson
Guest: Bill Tom Smith
Entertainer: Michael Johnson
Baker: Chris Jackson
Party Planner: Seema Patel
Publicist: Seema Patel
Baker: Ashley Sanders
'''
# no i mamy dwa imiona
pattern5 = re.compile(r'(?<!Baker: )(\b\w+\s\w+$|\b\w+\s\w+\s\w+$)',flags=re.IGNORECASE|re.M)
print('pattern5: ',re.findall(pattern5,string3 ))

print(' pull out the eintire string with occupation....look  ahead ?!')

pattern6 = re.compile(r'^(?!Baker: ).+\w+$',flags=re.IGNORECASE|re.M)
print('pattern6:', re.findall(pattern6,string3))

print('.....moje cwiczenia....')
stringM = "Dan has 3 snails. Mike has 4 cats. Alias has 9 monkeys."
print(re.sub(r'(?<=\s)\d(?=\s)','100',stringM))
print('................')
print(re.sub(r'(?<!\w)\d(?!\w)','999',stringM))

# tu ok, bochciałam ze jak jest przed liczba has to ma wyswietlic
print(re.findall(r'(?<=has )\d\s\w+',stringM))

# nie wyswietli 3,4,9, bo jak jest przed strigiem has to nie wyswietlaj
print(re.findall(r'(?<!has )\b\w+\b',stringM))
