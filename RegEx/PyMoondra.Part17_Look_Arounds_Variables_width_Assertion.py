import re
string = '''1111    ABCC    777777777      active
            2222    Abc     888888888      inactive
            3333    Xyz     xxxxxxxxx      active
            4444    1234    203511118      inactive
            5555    1445    201533181      inactive'''

# look behind wymaga okreslenia dlugosci, niemozna + stawiac
# pattern = re.compile(r'(?<=[A-Z]+)[A-Z]+\s+(\S+)')
# print(re.findall(pattern,string))

import regex
pattern = regex.compile(r'(?<=[A-Z]+)[A-Z]+\s+(\S+)')
print(regex.findall(pattern,string))