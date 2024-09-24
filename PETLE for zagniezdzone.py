
print('.......................petla 4444444444444444444444')
s = 0
# petla pierwsza z (x),mówi ile razy ma sie wykonac, i jesli nie ma x przypisanej wartoci, to ma wartosc z zakresu, czyli
# gdyby nie byłotu x =0, to x przyjmowały wartosci 2,3,4
for x in range (2,5):
   #d = 2
   print ('XX', x)
   for y in range (1,3): # tu y przyjmuje wartosci z petli, czyli y = -1, y =0
       # print('Y', y)
       d = x + y  # tu X zmienia wartosc i wchodzi znow dop petli for z ta wartoscia
       # print("x+y",d)
       s = s + d
       # dlakazdego y drukuje sume
       print ("wynik dla kazdego osobnego y: ",s)
    # dlakazdego x drukuje sume, czyli w tym przypadku z dwóch y
   print(("suma dla kazdego x: ",s))
# drukuje sume koncowa
print("suma koncowa: ", s)

print('.................................................petkla66666666666666666')

for i in range (1,11):
    print (i, end=' ')
print('\n')

for i in range (1,11):
    i = 99
    print(i, end=' ')
print('\n')


print("...............................??????????...dlaczegi nie dukuje 10,11,12,13..")
for z in range (1,11):
        print(z +10, end=' ')
print('\n')

for z in range (11,21):
        print(z, end=' ')
print('\n')

x=10
while x<20:
    x += 1
    print(x)




print("..........................................kkkkkkkklk........")

for i in range (1,11):
    for k in range(1,5):
        k *=2
        print (k, end=' ')
    print('\n')


print('.......................petla 3333333333333333')

s = 2
for x in range (1,2):
   for y in range (5,7):
      s = s + x + y
      print (s) # w tym momencie to s = 8, i ponownie wchodzi do petki jako 8


print ("..........................")
s = 2
for x in range (1,2):
   for y in range (5,7):
      s = s + x + y
print (s)


print('.......................petla 22222222')

s = 0
for x in range(1,3):
    print("xx", x)
    for y in range(1,4):
        print("y",y)


print('.......................petla 111111111111')
# s = 2
for x in range (1,2):
    print('XX', x)
    for y in range (5,7):
        print('YY',y)
        s = x + y
    print (s)