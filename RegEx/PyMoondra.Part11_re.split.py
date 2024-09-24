import re
zdania = 'Today is  sunny. I want go to the park. I want to at ice cream.'

# normanie rodziela i usuwa split point, czyli w tymprzypadku usunal kropke
print('1: ', re.split(r'\.', zdania))

# jak wezmiemie split point w nawaiasy, to wyswietli kropkę,ale jako oddzielny element
print('2: ',re.split(r'(\.)', zdania))

s = '*'
print('3: ',[i+s for i in re.split(r'\.', zdania)])

# cos trudniejszego <>, pomiedzy moga byc rozne rzeczy

string = '<p>My mother has <span style="color:blue">blue</span> eyes.</p>'
# doens't work
print('4: ',re.split(r'<\w+>',string))
# tez zle bo kropka zastepouje wszytskie znaki
print('5: ',re.split(r'<.+>',string))

# to teraz mamay <> a w srodku character set
# calkiem niexle ale mamy jeszcze spacje
print('6: ',re.split(r'<[^<>]+>',string)) # wyslwietl wsztsko  POZA tym co jest w <>

# jak usuwa cos z poczatku albo z konca, tozsotawia pusty string


print(re.split(',',',happy, birthday,'))


# zeby usunac ten pusty string uzywamy list comprehension
print("...................list comprehension zeby usunac pusty string z poczatku i konca.............")
# zachowaj 'i; jesli 'i' nie jest pustym stringiem
print([i for i in re.split(r'<[^<>]+>',string) if i !=''])

print('..........................................findall............zamiast........... split')
string = '<p>My mother has <span style="color:blue">blue</span> eyes.</p>'
#
print(re.findall('>([^<]+)<',string))
print('..........................................filter............zamiast........... split')
string99 = ',happy, birthday,'
print(list(filter(None, string99.split(','))))

