print(" and ".join(["a", "b", "c"]))
print(", ".join(["a", "b", "c"]))

print("Hallo World".replace("Hallo", "Witaj"))

print("To jest zdanie".startswith("To"))

print("To jest zdanie.".endswith("zdanie"))

print("e" in "To jest zdanie")

print("To jest zdanie".upper())
print("To jest zdanie".lower())

print("..........................nowe cwicznie ")

lista = [10, 20, 25, 30, 40]

if all([ i % 2 == 0 for i in lista]):
    print("wszytskie parzyste")
else:
    print("rozne")

if any([i %2 == 0 for i in lista]):
    print("jest jakas parzysta")

for i in enumerate(lista):
    print(i)

for i in (lista):
    print(i)

for i in enumerate(lista):
        print(i[0] +1, "-", i[1])

print ("........................................")
str5 = "/*Jon is @developer & musician since 1999"

str555 = ''.join([i for i in str5 if i.isdigit()])
print(str555)