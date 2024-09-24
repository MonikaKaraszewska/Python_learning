class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("hi, jestem", self.name, 'and I am', self.age, 'lat')

    def talk(self):
        print('bark')

print('..............................cat class')
class Cat(Dog):
    def __init__(self, name, age, color):
        # super().speak()
        super().__init__(name,age)
        super().speak()
        self.color = color

    def talk(self):
        print('meow!')


tim = Cat('tim', 5, 'blue')
print("...............................kot speak")
tim.speak()
tim.talk()

jim = Dog('Jim', 88)
jim.speak()
jim.talk()

print(" ...............................class vehicle")

class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas

class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price,gas, color)
        self.speed = speed

    def beep(self):
        print("Beep beep beep")


class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print("Honk honk")

traktor = Truck(34,78,'black',6)
traktor.beep()

maluch = Car(34,78,'blue',6)
maluch.beep()

print(isinstance(traktor,Vehicle))
print(type(maluch))
print(issubclass(Car, Vehicle))
print(issubclass(Car, Truck))