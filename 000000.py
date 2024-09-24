imie = input("give the name for the first time: ")
imie2 = input("give the name for the second time time: ")

# imie = "monika karasz"
# imie2 = "madzik joanna"

imie_nazwisko = imie.split()
imie_nazwisko2 = imie2.split()

imiona = list(zip(imie_nazwisko,imie_nazwisko2))
print(imiona)

new_imie = str(imiona[0][0][0:2])
new = imiona[0][1][-2:]
nazw1 = str(imiona[1][0][0:2])
nazw2 = (imiona[1][1][-2:])


print(f'{new_imie.title()}{new} {nazw1.title()}{nazw2}')