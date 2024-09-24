lista = [1,2, "c", "d", "e",]
print (lista)
print(lista[4])
lista[2] = 3
print(lista)
tekst = "hello world"
print (tekst[4], tekst[6], tekst[8])

# przypisanie na teraz elementów do listy
print(lista+["f", "g"], "tymczasowa")
print(lista)

# przypisanie na stałe elementów do listy
lista += "f","g"
print (".....................lista razy 3.....")
print(lista*3)
print("ilosc elementow:", len(lista))
print(lista)

# dolacz na stale element do listy
lista.append ("h")
print(lista)

# dolacz druga liste
lista.append(["i", "j", 9,8])
print(lista)
print("ilosc elementow na liscie: ", len(lista))
print("coto :", lista[8][1])  # wysiwetla e z elementu 8,czyli drugiej listy,element o idekcie 1, czyli 'j;
print("kurde Nooo", lista)
print("A teraz? :", lista[1],lista [2]) # zeby wyslwietlic dwa elementy z tej samej listy
print(lista[8])
print("....insert.....")
lista.insert(3,33)
print(lista)
print("ilosc: ", lista.count(2))
print("index:", lista.index("h"))
lista.remove("f")
print("TU", lista)
print ("...................................................................kawalki listy...........................")
print(lista[2:5])
print("w:",lista[2:])
print(lista[:4])

print("??",lista)
# print(lista.index[6])
lista[6] = "8" # zamienia na liscie to co jest na ideksie 6
print(lista)
lista2 = [1, 20, 35,-5, 0]
print("min: ", min(lista2))
print("max: ", max(lista2))
lista2.sort()
print(lista2)
lista2.reverse()
print(lista2)
lista2.clear()
print(lista2)
lista.append("tata")
print(lista)
lista.insert(4, "mama")
print(lista)
print('[-1]' ,lista[-1])
print('[:-1]' ,lista[:-1])
print('[::-1]' ,lista[::-1])

print(lista[4])

lista.remove("h")
print(lista)
print("............................................................................tu jestes")
for element in lista:
    print(element)
print(lista)

lista.pop(5) # usuwa element o podanym indeksie
print (lista)

print("......................................")
lista8 = [88,90,45,77]
lista3 = lista + lista8
print(lista3)
print("......................................")


#sort działa tylko jak w lisice sa elelemnty albo tylko string albo  tylko liczby
lista8.sort()
print(lista8)

lista8.sort(reverse=True)
print(lista8)

print('.....................swap.......................')
lista1= [12, 35, 9, 56, 24]
def swap_indx(lista1,i1,i2):
        lista1[i1], lista1[i2] = lista1[i2], lista1[i1]
        print(lista1)

swap_indx(lista1,0,4)