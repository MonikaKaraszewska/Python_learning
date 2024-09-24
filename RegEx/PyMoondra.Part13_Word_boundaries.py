import re

#\b - b odnosi sie do boundaries, check position and locations

string  = "cat cathrine catholic wildcat copycat uncatchable"

pattern = re.compile('cat')

print("pat1: ",re.findall(pattern,string))

pattern2 = re.compile(r'\bcat\b')
print("pat2: ",re.findall(pattern2,string))

print('')
## uwaga na kropki i non-alphanumerc characters (+:@^%) czli toco nalezy do \W
#\w do tego naleza litery liczby i _
string2  = ".cat cat @cat cathrine catholic wildcat%$ copycat uncatchable"
print("pat32: ",re.findall(pattern2,string2))
# \b sprawdza ,po jednej stronie ma byc alphanumerc characters a po drugiej ma byc NONalphanumerc characters
pattern3 = re.compile(r'\bcat\w+')
print("pat3: ",re.findall(pattern3,string2))

pattern4 = re.compile(r'cat\b')
print("pat4: ",re.findall(pattern4,string2))

pattern4 = re.compile(r'\w+cat\b')
print("pat5: ",re.findall(pattern4,string2))

