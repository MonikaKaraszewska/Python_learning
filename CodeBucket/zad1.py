a = int(input("podaj liczbe a:"))
b = int(input("podaj liczbe b:"))
c = int(input("podaj liczbe c:"))

sum1 = a + b
sum2 = a + c
sum3 = b + c

if sum1>c and sum2 >b and sum3 >a:
    print("mozesz zbudowac trojkat")
else:
    print("NIE mozesz zbudowac trojkata")