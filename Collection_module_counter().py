import collections
from collections import Counter

c = Counter("gallad")
print(c)
h = Counter(['a', 'a', 'b', 'c', 'c'])
print(h)
print("elements h: ",list(h.elements()))
f = Counter({'a' : 1,'b' : 2})
print(f)
print("elements f: ",tuple(f.elements()))
e = Counter(cats = 4, dogs = 7)
print(e)
print("elements e: ",list(e.elements()))

d ='Przeglądając nowe kategorie i spersonalizowane rekomendacje, łatwiej znajdziesz idealne motywy i rozszerzenia pomagające dostosować przeglądarkę. Otwórz menu Chrome . Wybierz Rozszerzenia, a następnie Zajrzyj do Chrome Web Store. Przeglądaj rozszerzenia i motywy, dzięki którym dostosujesz Chrome do swoich potrzeb.'
c = Counter(d.lower())
print(c)

print("...................................")

print("most_common h: ", h.most_common(1))

print("most_common c: ", c.most_common(3))

print(".....................counters")
''' Metoda subtract służy do odjęcia wartości z innej instancji Counter lub z innego obiektu, który może być 
przekształcony na Counter.
Wartości zostaną odjęte z pierwszego licznika na podstawie drugiego. Jeśli wartość klucza w drugim liczniku 
jest większa niż w pierwszym, to ostateczna wartość będzie ujemna.
'''
g = Counter(cats = 9, dogs = 3)
e = Counter(cats = 4, dogs = 7)
g.subtract(e)
print(g)

print(".........update...czyli dodaje")
kl = Counter(['a', 'a', 'b', 'c', 'c'])
kj = Counter({'a' : 1,'b' : 2})

kj.update(kl)
print(kj)
kj.clear()
print(kj)

g2 = Counter(cats = 9, dogs = 3)
e2 = Counter(cats = 4, dogs = 7)

print(g2 + e2)
d3 = Counter(['a', 'a', 'b', 'c', 'c'])
f3 = Counter({'a' : 1,'b' : 2})
# jesli wychodziponiez zera albo 0, to w ogole nie bedzie pokazane
print(f3-d3)

print("................intersections")
# show minimum
print(g2 & e2)
print(d3 & f3)

print("............union|....")
# max elements show in each of a counters
print(g2 | e2)
print(d3 | f3)


print(".....moje")
r ='Wybierz Rozszerzenia, a następnie Zajrzyj do Chrome Web Store. Przeglądaj rozszerzenia i motywy, dzięki którym dostosujesz Chrome do swoich potrzeb.'
z ='Przeglądając nowe kategorie i spersonalizowane rekomendacje, łatwiej znajdziesz idealne motywy i rozszerzenia pomagające dostosować przeglądarkę. Otwórz menu Chrome . Wybierz Rozszerzenia, a następnie Zajrzyj do Chrome Web Store. Przeglądaj rozszerzenia i motywy, dzięki którym dostosujesz Chrome do swoich potrzeb.'
r = Counter(r)
z = Counter(z)
print(z & r)