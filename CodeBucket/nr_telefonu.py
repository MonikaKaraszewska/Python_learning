nrTelefonu = (input("podaj numer telefonu: "))
print(nrTelefonu)
if "-" in nrTelefonu:
    nrTelefonu = nrTelefonu.replace("-","")
if " " in nrTelefonu:
    nrTelefonu = nrTelefonu.replace(" " ,"")
print("ico wyszlo?:", nrTelefonu)