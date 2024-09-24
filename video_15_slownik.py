mojslownik = {1: "nie lubie poniedzialkow", 2: "wtorek", 5:"piatek", 7:"niedziela", "john wick": 362541}

print(mojslownik[1])
mojslownik[3] = "sroda"
mojslownik[4] = False
mojslownik[6] =6
mojslownik["a"] = 1
print(mojslownik)
print(mojslownik["a"])

print("get: ", mojslownik.get(5)) #pokazuje value, toco w nawaisie to klucz
print(mojslownik[5])
print(mojslownik)

print("\nPętla:")
for l in mojslownik.values():
    print(l)

print("\n....................")
print(mojslownik.pop(2)) #usuwa elementy
print(mojslownik)


print(".........a nested dict. Use the correct chaining of keys to locate the specified key-value pair............")
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])

print("...............................................POP...............")
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
print(sample_dict.pop('age'))
sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

list1 = ["M", "na", "i", "Ke"]
list1[1] = list1.pop(3) # tym sposobem na ideksie 1 jest wartsczwrocona przez pop, pop usunał ke na 3 miejscu
# i zwrócił wartosc "ke',która przypisałan do miejsca 2
print(list1)

print(".........................................................laczenie dwoch slownikow")
dicki = {"Asia": "asia@gmail.com",
         "Madzia": "magda@gmail.com",
         "Pawcio": "pawel@gmail.com"}
mojslownik = {1: "nie lubie poniedzialkow", 2: "wtorek", 5:"piatek", 7:"niedziela", "john wick": 362541}

slownik55 = {**dicki,**mojslownik}
print(slownik55)

print("........................setdefault")
# setefault - dodaj jesli takieg klucza nie ma go w słowniku, jesli istnieje nie zmienie nic, nie nadapisze value

mojslownik.setdefault('x',100)
print(mojslownik)

#jesli istnieje nie zmienie nic, nie nadapisze value
mojslownik.setdefault('x',567)
print(mojslownik)

# update zmienia
mojslownik.update({'x': 345})
print(mojslownik)