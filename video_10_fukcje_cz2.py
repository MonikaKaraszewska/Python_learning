def func(x):
    print(x)
#    return x * x

# zmienna = func
# print(zmienna(5))

# def func2(fu1, y):
#     wynik_fu1 = fu1(y)
#     return wynik_fu1 * y

def func2(y):
    func(y)
    wynik = y * y
    func(wynik)
    return wynik

print(func2(5))
#print(func2(func,5))


# # rekurencja, czyli funkcja wywołuje siebie
def dupa(x):
    print("wchodze w dupe z argumentem " + str(x))
    if x <= 1:
        print("zwracam 1")
        return 1
    else:
        w = x * dupa(x-1)
        print("zwracam " + str(w))
        return w
print(dupa(4))
# print(silnia(6))