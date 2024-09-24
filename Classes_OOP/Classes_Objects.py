x='strings'
y=4

"""x, y sa obijektami, x jest objektem klasy string, y jest objektyem klasy intiger"""


print(type(x))
print(type(y))

''' jak piszmy x.  kropka wywołuje metody jakie sa wbudowane w klase string, i tu mamy count, find,len...'''

print(x.count('s'))
print(y.bit_count())


print("..............................class dog..........")

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [1,2,3,4,4]

    def speak(self):
        print("hi, jestem", self.name, 'and I am', self.age, 'lat')


    def change_age(self,age):
        self.age=age


    def add_waga(self,waga):
        self.waga = waga


tim = Dog('Tim', 55)
fred = Dog('Fred', 6)
tim.change_age(33)
tim.add_waga(77)

print(tim.waga)
print(fred.waga)

tim.speak()
fred.speak()

# tim.waga

print(tim.age)
print(tim.name)
print(fred.li)
print(tim.li)
