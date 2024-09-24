'''deque (double-ended queue) jest strukturą danych dostępną w module collections w języku Python. Oferuje ona wiele przydatnych funkcji, w tym:

append(x): Dodaje element x na koniec kolejki.
appendleft(x): Dodaje element x na początek kolejki.
clear(): Usuwa wszystkie elementy z kolejki.
copy(): Tworzy kopię kolejki.
count(x): Zwraca liczbę wystąpień elementu x w kolejce.
extend(iterable): Rozszerza kolejkę o elementy z podanej iterowalnej kolekcji.
extendleft(iterable): Rozszerza kolejkę o elementy z podanej iterowalnej kolekcji, dodając je na początek kolejki.
pop(): Usuwa i zwraca ostatni element kolejki.
popleft(): Usuwa i zwraca pierwszy element kolejki.
remove(value): Usuwa pierwsze wystąpienie wartości value z kolejki.
reverse(): Odwraca kolejność elementów w kolejce.
rotate(n=1): Przesuwa elementy kolejki o n miejsc w prawo, przy użyciu wartości ujemnej przesuwa w lewo.
maxlen: Atrybut określający maksymalną długość kolejki.
deque jest szczególnie przydatny w przypadku, gdy potrzebujesz struktury danych, która umożliwia efektywne dodawanie i usuwanie elementów z obu końców kolejki.'''



import collections
from collections import deque

d = deque("hello")
d.append("4")
print(d)
d.appendleft("7")
print(d)
d.rotate(2)
print(d)
d.rotate(-3)
print(d)

