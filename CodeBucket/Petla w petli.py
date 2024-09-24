# piersza petla mówi ile rzedow, a duga petla ile w rzedzie ma byc
print(".....................................fotelew kinie")
for i in range (0,3):
    for j in range (0,20):
        print("*", end='')
    print('\r') # tojest enter

print(".....................................fotele ciag dalszy................")
for i in range (0,3):
    for j in range (0,5):
        print(i+1, end='')
    print('\r') # tojest enter

print("........................................gwiazdki..............")
for i in range (0,4):
    for j in range (0,i+1):
        print("*", end='')
    print('\r')

print("................................trójkat z........gwiazdki..............")
n=5
for i in range (0,n):
    for j in range(0,n-(i+1)):
        print(end=" ")
    for j in range (0,(i+1)):
        print("*", end='')
    print('\r')