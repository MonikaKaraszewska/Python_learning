import re
# Character sets
# \w - matches alpha numeric characters A-Z, a-z 0-9 i _ underscore \w - jedno takie = jeden znak

print(r"............................................................alphaNumeric \w.- 'w' z malej litery.")
alphaNumeric = re.search(r'\w\w\w\w','abcdefg abc')
print("alphaNumeric: ",alphaNumeric)

alphaNumeric1 = re.search(r'\w\w\w\w','ab_cdefg abc') # underscorde nalzey do tego set
print("alphaNumeric1: ",alphaNumeric1)

alphaNumeric2 = re.search(r'\w\w\w','a3.!-!')
print("alphaNumeric2: ",alphaNumeric2)

alphaNumeric3 = re.search(r'\w\w\w','a33-!').group()
print("alphaNumeric3: ",alphaNumeric3)

print(r"............................................................alphaNumeric \W.- 'W' z WIELKIEJ litery.")

# \W jest przeciwienstwiem \w - czyli wyszukaj wszytsko poza tym co jest w zbiorze \w

W_opposite_w = re.search(r'\w\w\W\W','a3!.-_!')
print("W_opposite_w: ",W_opposite_w)

W_opposite_w1 = re.search(r'\w\w\W\W','a3 !.-_!') # \W -matches empty spaces AS WELL
print("W_opposite_w1, with empty spaces: ",W_opposite_w1)

# Quantifiers

print(r"...................ile razy chce cos powtorzyc.............................................................Quantifiers................")
    # '+' = 1 or more
    # '?' = 0 or 1
    # '*' = 0 or more
    # '{n,m}' =n to m repetition {,3},{3,}
print(r".....................................................................................plus................")

plus = re.search(r"\w+", "abc3456_6defnc a566bcd") # plus to greedy quantifier
print("plus: ", plus)

plus1 = re.search(r"\w+\W+\w+", "abc36_6defnc a5bcd") # \W wyszuka spacje
print("plus1: ", plus1)

plus2 = re.search(r"\w+\W+\w+", "abc3_defnc                a5bcd")
print("plus2: ", plus2)

print(r".....................................................................................??????................")

znakZapytania = re.search(r"\w+\W?\w+", "ab cdefncabcd").group() # ?moze byc ale nie musi np moze byc spacja ale nie musi
print("znakZapytania: ", znakZapytania)

znakZapytania1 = re.search(r"\w+\W?\w+", "ab   cdefncabcd").group() # ? znak zapytania mowi 0 albo jedna, ale jak jest wiecej jak 1 to juz nie wyswietli dalej do pierwszej tylko
print("znakZapytania1: ", znakZapytania1)

znakZapytania2 = re.search(r"\w+\W+\w+", "abcdefncabcd") # w tym mamy \W+ wiec musi byc chociaz jeden z tegozobioru, nie ma wiec wysiwetla NONE
print("znakZapytania2: ", znakZapytania2)

print(r".....................................................................................pulling out specific amounts...{}............")
klamerki = re.search(r"\w{3}", "aa bbbb ccccaaaaaaa").group()
print("klamerki: ", klamerki)

klamerki1 = re.search(r"\w{2,4}", "aa bbb ccccaaaaaaa").group() #{a,b} a minimalna, b maksymalna ilosc
print("klamerki1: ", klamerki1)

klamerki2 = re.search(r"\w{1,}\W{,2}\w{1,5}\W\w{1,3}\W{0,5}\w", "aaff bbbu ccc  a").group()
print("klamerki2: ", klamerki2)