'''     %s -string
        %d = integers
        %f - float number
        %.(number of  digits)f - float point numbers with a fixed number of digits to the right
        %x / %X - integers in hex representation )lowercase/uppercase)
        %o - octal'''

name = 'Monika'
print("hello,%s" % name)

print("hello, %s %s. your current balance is $%f" % ("Holden", "ford", 8123546))

data=("Holden", "ford", 812732663)
format_string = "Hello, %s %s. your current balance is $%.3f"
print(format_string % data)

'''general arguments
    %[key][flags][width][.precision][length type][conversion type] %[value]
    1.'%' marks the begining of he argument specifier
    2. key  
    3. Flags
    4. Width - specifies the total number of characters to be shown
    5. Precision: specified be '.', how many float values you want to display
    6. Length type: Not importnat
    7. conversion type ;this specifies the datat type (%d,%s)
    8. %value - values you want to substitute for the conversion types'''

print("......................................use of keys...................")
dct = {'foo': 10, 'bar': 20}
print("%(foo)s" % dct)
print("......................................use of width...................")
# 2 and 4 are widths
# jak chemy zeby zarezerwowoal 2miejsca '%2d', a nasza liczba ma 3elementy to i tak wyswietli tyle ile jest w danych
# # jak chemy zeby zarezerwowoal 4 miejsca '%4d', a nasza liczba ma 3elementy to dodta dodatlowe spacje zeby sie zgadzalo
print("total number of students: %2d. Total number of girls: %4d" %(240,120))

print("..................................octal ..................")
print("An OCtal:%7o" %25)

print("..................................example of using asterisk ***** ..................")
# ** taks any amonunt of charachters
print('|%*s| = |%*f|' % (10,'ABCD', 13, 171.8269))

print("..............................................flags ..................")
# '0' zero flag - puste miejsca beda wypelnione 0, zerem
print('%5d'%1)
print('%05d'%1)

# usunie 0,puste miejsca po lewej ijednyka bedzie na piwerszym miejscu, ale ze zarezerowowane mamy 5 miejsc,
# to te miejsca beda po  prawej, po value

print('%5d'%1)
print('%-5d'%1)

print('% d'%1) # jedna spacje mozna wrzucic,aledwie juz nie bedzie dzialac
print('% d'%-1)
print('% d'%+1)

print('%+d'%+1)

print("...................precision...........")
# precision is specified as a '.' (dot) followed by number of idgitd required after decimal. '*' is viable(wykonalny)
print("Your id is: %3d. Your score is: %4.2f" %(13,05.33333))

print('ABCD stock price: %.2f' % 1999.83762552)
# '*'(asterisk) pierwszy asterisk pobiera value 3 a drugi 4,dlatego wyswietla tylko BMI
print("An example using asterisk: %.*s = %.*f" %(3, 'BMI_index', 2, 171.8269))

print("...................................E ...exponential value.........")
# E - Exponent form
'''What does it mean if something is exponential?
an extremely rapid increase'''
print("%13.3E" % (322.1249973663))
print("%2.5E" % (7656.83778363))


print('')
print("|%11.7s" % ('formatting'))
print("%-11.6s|" % ('formatting'))