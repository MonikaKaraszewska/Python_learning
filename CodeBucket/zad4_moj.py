def moje_franki(kwota, kurs):
    suma = round(kwota * kurs,2)
    return suma
print(moje_franki(13.77,4.75))


def na_franki(*kwoty, kurs=4.65): # mozemy podac kilka kwot
    kwoty_przewalut = []
    for kwota in kwoty:
        suma = round(kwota * kurs,2)
        kwoty_przewalut.append(suma)
    return kwoty_przewalut

print(na_franki(15,23,14,28))



