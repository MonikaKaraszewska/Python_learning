litsa = [(1, (2.3, 4.3)), (4, (1.3, 6.3)), (2, (0.3, 9.3))]

k = lambda x:x[1][1]

litsa.sort(key=k, reverse=True)
print(litsa)


# Definicja lambda funkcji
add = lambda x,y,z: x + y/z

# Użycie lambda funkcji
result = add(3, 5, 2)
print(result)
print(bin(-33))
print(hex(-333))
print(oct(-333))
