import re
searching_c = re.search('c','abcdefc')
print("searching_c:", searching_c)


matching_c = re.match('c','abcdef')
print("matching_c: ",matching_c)

print(bool(re.match('c','abcdef')))

#multiline works with search
multiline_search = re.search('c','abdedf\nc')
print("multiline_search",multiline_search)

#multiline doesn't works with match
multiline_match = re.match('c','abdedf\nc')
print("multiline_match: ",multiline_match)

print("..................................................printing the output of match and search")
# to print the output we need to add group

outputSearch = re.search('c','abcdedf gbcd').group()
print("outputSearch : ",outputSearch )

outputMatch = re.match('a','abcdedfc').group()
print("outputMatch: ",outputMatch)

startIndex = re.search('c','acbdedf ghy gc').start()
print("startIndex: ",startIndex)

endIndex = re.search('c','abdedf ghy gc').end()
print("endIndex: ",endIndex)

print(".................................................lazy dog.........")

string = "The quick brown fox jumps over the lazy dog."
pattern = r"brown.fox"

match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")


print("..................................................literal matching..re.search.........")
literalsearch = re.search('abc','abcc abccdedfc abc') # wyszuka tylko pierwszy match
print("literalsearch: ",literalsearch)

literalsearch2 = re.search('a|c','fbcdedfc abc')# wyszuka tylko piersza zpodanych i tu bnedzie 'c'
print("literalsearch2: ",literalsearch2)

literalsearch3 = re.search('a|j|d','fbcdedfc abc').group()# mozna wiecej dac do wyszukania
print("literalsearch3: ",literalsearch3)

print(".....................................................................re.findall........")
# wyszuka wszytskich i wyswietli jako lista
findAll = re.findall('a|c','fbcdedfc abc')
print("findAll: ",findAll)

findAll1 = re.findall('abc','abcdedfc abc')
print("findAll1: ",findAll1)