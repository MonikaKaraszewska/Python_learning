import re

# other types of characters sets

# '''\d' = matches digits [0-9]
# '\D' = the opposite of d\, it means it matches any non-digit character'''

digitSearch = re.search(r'\d+', "23ab89cded++").group()
print("digitSearch: ", digitSearch)

digitSearch1 = re.search(r'\D+', "23a!b89cded++").group()
print("digitSearch1: ", digitSearch1)

print(".......................................................whitespace......")
# '\s' - matches any whitespace characters,newlines, tabs, spaces etc
# "\S" - matches any NOn-whitespace characters
spaceSearch = re.search(r'\S+', "2a!b89c ded++") # find all what is not empty space
print("spaceSearch: ", spaceSearch)

tekst = '''Many of those gaps result from the coarse-grained approximations that admins rely on to manage identity, authentication, and access at scale. Instead of impeding users, admins will over-provision accounts from the start or maintain access longer than required for users to perform their roles.
         Advertisements Humans can’t manage users’ permissions and entitlements second-by-second.
         But AI can. In fact, unlike humans, AI improves with greater volumes of data as it learns users’ behaviors and organizational context.
         AI can make the fine-grained, just-in-time decisions needed to move closer to zero-trust architecture and adapt to modern threats.
         We’ve seen great potential in using AI to evaluate authentication requests, entitlements, and usage activity.
         Ghai elieves organizations will need those AI-powered capabilities as a core component of their cybersecurity architecture.'''

result = re.findall(r'\S+',tekst)
print(result)
tekstBACK = ' '.join(result)
print("tekstBack:", tekstBACK)

print(".......................................................dot......")
# dot matches any character except the newline, czyli wyswietli z pierwszejlinijki, jak jest nowa linia juz nie bedzie
dot = re.search('.+', tekst).group()
print("dot: ",dot)

dotFlag = re.search('.+', tekst, flags=re.DOTALL).group()
print("dotFlag: ",dotFlag)
print(" ")
print("........................................................creating own character sets....")

string = "Hello, There, How, Are, You"
stringSet = re.findall('[A-Z]',string)
print("stringSet: ", stringSet)

string2 = "Hello, There,7. How, 9.Are9, You...."
stringSet2 = re.findall('[A-Z,.]',string2)
print("stringSet2: ", stringSet2)

string2 = "Hello, There, How, Are, You...."
stringSet3 = re.findall(r'[A-Za-z+,\s.]',string2)
print("stringSet3: ", stringSet3)
print(' ')

print("...The sub() function replaces the matches with the text of your choice:..........sub.....")

txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt)
print(x)
substriing2 = re.sub('e','*',string2)
print(substriing2)
substriing33  = re.sub('e','*',string2,3)
print("substriing33: ", substriing33)
print('  ')

print("The split() function returns a list where the string has been split at each match:./.....split")

adres = '000.192.1508.1.308'
x = re.split(r"\.", adres) # albo [.]
print(x)
y = re.split("0", adres)
print(y)

#[+]In sets, +, *, ., |, (), $,{} has no special meaning,
# so [+] means: return a match for any + character in the string