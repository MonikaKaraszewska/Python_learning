import re
print("...................................consecutive look around  fallacy...")
string = '''cherry 100 red
            apple 150 green
            grapes 200'''

pattern  = re.compile(r'[a-z]+\s*(?=\d+)\s*(?=[a-z]+)') # nic nie wyswietla bo sa dwa lookahead,no i pierwszy
# sie rozglada za liczbami i wraca,wiec nie wypelnia drugiego warunku w lookahead
print('pattern: ', re.findall(pattern,string))

# zeby sprawdzil czy sa liczby i kolor, musimy w jednej prupie umiescic z jednym looka round

pattern2  = re.compile(r'[a-z]+\s*(?=\d+\s*[a-z]+)')
print('pattern2: ', re.findall(pattern2,string))


print(".....................................................................good for password validation..............")
## przy wpisywaniu hasla, jest ze ma byc jeden z wielkiej litery, z malej, liczba, i jakis znaki to wlasnie sprawdza
# i na koncu wysiwetla wszytsko jak sue zgadza \S+ - czywli wszytsko co nie jest spacja
pattern3 = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!?.])\S+')

string2 = 'AZN#3232!abbb32..'
string3 = 'AZN#3232abbb32'

print("string2: ", re.search(pattern3,string2))
print("string3: ", re.search(pattern3,string3))


