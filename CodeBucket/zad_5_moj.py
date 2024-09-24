wyrazy = open("wyrazy.txt", "r")
# print(wyrazy.read())
wykaz = []
wykazodwr = []
palindromy = []
for i in wyrazy:
    # if i not in wykaz:
    i=i.strip()
    wykaz.append(i.replace("\n", ""))
    #for k in i:
    odwroce = i.replace("\n", "")[::-1]
        # if odwroce not in wykazodwr:
    wykazodwr.append(odwroce)

for i in wykaz:
    if i in wykazodwr:
       palindromy.append(i)

print("palin",palindromy)
print("wykazodwr", wykazodwr)
print("wykaz", wykaz)

palin = open("palin.txt", "w")
palin.write(str(palindromy).replace(" ", "\n"))

yesNo = open("yesNo.txt","w")
for i in wykazodwr:
    if i in wykaz:
        yesNo.write("tak" + "\n")
    else:
        yesNo.write("nie" + "\n")

print("palin", len(palindromy))
print("wykaz",len(wykaz))
print("wykazdowr",len(wykazodwr))