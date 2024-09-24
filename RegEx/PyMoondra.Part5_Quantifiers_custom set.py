import re
string = "HELLO, The7re, How, Are You...."

stringSearch = re.search('[A-Z]+',string)
print("stringSearch ", stringSearch)

stringFindAll = re.findall('[A-Z]+',string)
print("stringFindAll: ", stringFindAll)

stringFindAll2 = re.findall('[A-Z]{2,}',string)
print("stringFindAll2: ", stringFindAll2)

stringFindAll3 = re.findall(r'[A-Za-z\s]+',string)
print("stringFindAll3: ", stringFindAll3)

string = "HELLO, There, How, Are You...."

stringFindAll4 = re.findall(r'[A-Z]?[a-z\s,]+',string)
print("stringFindAll4: ", stringFindAll4)

stringFindAll5 = re.findall(r'[^A-Za-z\s,]+',string) #[^] neguje wszytsko co w srodku
print("stringFindAll5: ", stringFindAll5)

stringFindAll6 = re.findall(r'[^A-Z]+',string)
print("stringFindAll6: ", stringFindAll6)