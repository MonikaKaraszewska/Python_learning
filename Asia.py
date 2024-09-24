import re
input = '192.1688.0.1'
print(bool(re.findall(r'(?=\d{3}\.\d{3}\.\d{1}\.\d{1}$)',input)))

if bool(re.findall(r'(?=\d{3}\.\d{3}\.\d{1}\.\d{1}$)',input)):
    print("valid")
else:
    print('invalid')


inputTuple = ((5, "TutorialsPoint"), (6, "Python"), (7, "Codes"))
print("The input Tuple:", inputTuple)

# Here we are iterating through each element (pairs) of the tuple using dictionary comprehension and converting it to the dictionary
resultDictionary = dict((x, y) for x, y  in inputTuple)
print("The result dictionary:", resultDictionary)