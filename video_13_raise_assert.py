def dzielenie(x,y):
    # assert y != 0, "Y==0"
    if y ==0:
        raise ZeroDivisionError("dzielenie przez 0")
    print(x / y)

try:
    dzielenie(8,0)
except ZeroDivisionError:
    print("jest blad baranie")
print("cokolwkkd")


