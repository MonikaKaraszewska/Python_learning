import re
import string
print(dir(string))
print('.......................string constants............')

print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
'''The string.printable constants return the combination of ascii_letters, digits, punctuations and whitespace.'''
print(string.printable)
print(string.whitespace)

print("...........................string.capwords() ")
''''''
txt = "Programming Funda is programming portal"
x = string.capwords(txt)
print(x)
print(txt.title())
