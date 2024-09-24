print("...............................................using 'format()' method.................")

name,age = 'Holden Ford', 34
string_template = "My name is {0} and I am {1} years old."
print(string_template.format(name,age))
print("Moj", f'Nazywam sie {name} and I am {age} lat.')

print('')
hobby1,hobby2 = "reading", "jumping"
str_templ = "My name is {} and I am {} years old. I enjoy {} and {}"
print(str_templ.format(name,age,hobby1,hobby2))
print("")
print("I am {} and I am {} years old. I enjoy {} and {}.".format(name,55,hobby1,hobby2))
print(f"MOje2: I am {name} and I am {55} years old. I enjoy {hobby1} and {hobby2}.")

print('')
print("Hello {name}, your weight is {weight} and i like {name}.".format(name="Alex", weight='88.56'))
print("Hello {name}, your weight is {weight:5.2f} and i like {name}.".format(name = 'alex', weight = 88.56789))

print('')
#{1:9.2f} 1: - zduga grupa i zaczynamy formatowanie, 9 oznacza precision argument,
print("Hello {0}, your weight is {1:9.2f}.".format("Alex",88.564355))
#':'colon onacza ropoczecie formatowania
print("......................................< ^ > used for alignment.................")
#  > right alignment (similar to default)
print("|{:>6d}|".format(15))
print("|{:6d}|".format(15))

print('')
'''alignment = uszeregowanie,uporzadkowanie, wyrówaie, wyregulowanie'''
# float number with center alignment
''' : start
    ^ center
    10 width
    .3f float'''
print("|{:^10.3f}|".format(15.31456))
print("|{:^10.3s}|".format('formatting'))

# left alignment
print("|{:<5d}|".format(12))
print("|{:<05d}|".format(12))
print("|{:<+5d}|".format(12))
# padding area is the space between its content and its border.
print(r".........................'='............. operator...równa się..........")
''' "=" forces the padding to be placed after the sign (if any) but before the digits
 it is used to for printing fields in the form '+0000000120'
 this alignment option is only valid for numeric types
 It becomes the default when '0' immediately precedes the field width'''

print("|{:=17.3f}|".format(-12.3617282))
print("|{:0=17.3f}|".format(-12.3617282))

print('')
print(' .............string formatting with string.........................')
# with left alignment everything pushed to the left and we have empty spaces on te right
print("|{:6}|".format('form'))
print("|{:<16}|".format('form'))
print("...............................right alignment..........")
print("|{:>16}|".format('form'))
print("...............................center alignment..........")
print("|{:^16}|".format('form'))

print("...............................center alignment....and padding '*' character......")
print("|{:*^16}|".format('form'))
print("|{:-^16}|".format('form'))

'''Truncation in IT refers to “cutting” something, or removing parts of it to make it shorter.'''

print('......................truncating strings ................. czyli przycinanie ............')
#truncating strings to 2 letters, czyli przycinanie do 2 liter
print("|{:.2}|".format('formatting'))

#truncating strings to 2 letters, and space padding
print("|{:5.2}|".format('formatting'))

#truncating strings to 2 letters, padding and center alignment
print("|{:^5.2}|".format('formatting'))

