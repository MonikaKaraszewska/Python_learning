print('......Python Simplified.....')

names =['Mariya', 'Gandalf', 'Batman']
prof= ['programmer', 'wizard', 'superhero']

slownik = dict(zip(names,prof))
print(slownik)
print("zip approach")
print({key:value for (key,value) in zip(names,prof)})
print(("range approach"))
print({names[i]:prof[i] for i in range(len(names))})

print(" dictionary comprehension")
my_dict = {
    "Spider": "photographer",
    "Bat": "philanthropist",
    "Wonder Wo": "nurse"
}

my_dict2 = {key+'man' for(key,val) in my_dict.items()}
print(my_dict2)

my_dict3 = {key+'man':None for key in my_dict}
print(my_dict3)

my_dict4 = {key+'man' if key != 'Spider' else "superman" for(key,val) in my_dict.items()}
print(my_dict4)

print('')
print("....................genetyka")
bases = ['A', 'T', 'C', 'G']
import random
strand1 = random.choices(bases, k=10)
print(strand1)

result = {key:[val,None] for (key,val) in enumerate(strand1)}
print(result)
print('')
dna = {key:[val,("T" if val == "A" else "A" if val =="T"
        else "C" if val == "G" else 'G')]
       for (key,val) in enumerate(strand1)}
print("DNA ",dna)
print('')
print(".......................................keys/users dictionary")
keys = ["id", "username", "password"]
users = ["mariyasha888", "KnotAbot",'batamnns']

data = [{key:(i if key=="id" else users[i]if key =='username' else None) for key in keys} for i in range(len(users))]
print(data)

import random
import string
print(string.printable)

password = ''.join(random.choices(string.printable,k=8))
print(password)
data2 = [{key:(i if key=="id" else users[i]if key =='username' else password) for key in keys} for i in range(len(users))]
print(data2)