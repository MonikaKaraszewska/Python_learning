import operator
from collections import namedtuple

data = [(9, 2), (4, 5), (6, 8)]
data.sort(key=operator.itemgetter(1))
print(data)


data1 = [(9, 2, 6), (4, 5, 3), (6, 8, 2)]
data1.sort(key=operator.itemgetter(1))
print(data1)

data2 = [(9, 2, 6), (4, 5, 3), (6, 8, 2)]
data2.sort(key=operator.itemgetter(0), reverse=True) #sortowanie będzie odbywać się w porządku malejącym (malejąco)
print(data2)

data2 = [(9, 2, 6), (4, 5, 3), (6, 8, 2)]
data2.sort(key=operator.itemgetter(0), reverse=False) #sortowanie będzie odbywać się w porządku rosnącym
print(data2)

print("...........................dane")
dane = [{'name': 'John', 'age': 25, 'salary': 50000},
        {'name': 'Alice', 'age': 30, 'salary': 60000},
        {'name': 'Bob', 'age': 22, 'salary': 55000}]

dane.sort(key=operator.itemgetter('age'))
print("Sort dane: ",dane)

max_ele = max(dane, key=operator.itemgetter('salary'))
print("Max element: ",max_ele)


print("................")

comments = ['Python is awesome', 'yeah', 'I prefer Python 3 over python2', 'Absolutely']

print(sorted(comments))

print("sorted by len: ",sorted(comments, key=len))
print("sorted by len reversed: ",sorted(comments, key=len, reverse=True))

print("............lsita z krotkami")

tuple_comment = [('Alice', 'Python is powerful', 42, '(2022, 2, 3)'),
 ('Bob', 'Python is versatile', 17, '(2022, 2, 3)'),
 ('Charlie', 'Python is easy to learn', 91, '(2022, 2, 3)'),
 ('David', 'Python is super', 69, '(2022, 2, 3)'),
 ('Eva', 'Python is awesome', 55, '(2022, 2, 3)'),
 ('Frank', 'Python is fantastic', 23, '(2022, 2, 3)')]


print(sorted(tuple_comment,key=operator.itemgetter(2)))
print("Lambda: ", sorted(tuple_comment,key=lambda comment: comment[2]))


print(".................slownie ")

slownik = [
 {'author': 'Alice', 'comment': 'Python is powerful', 'likes': 42, 'date': (2022, 2, 3)},
 {'author': 'Bob', 'comment': 'Python is versatile', 'likes': 17, 'date': (2022, 2, 5)},
 {'author': 'Charlie', 'comment': 'Python is easy to learn', 'likes': 91, 'date': (2022, 2, 7)},
 {'author': 'David', 'comment': 'Python is super', 'likes': 69, 'date': (2022, 2, 9)},
 {'author': 'Eva', 'comment': 'Python is awesome', 'likes': 55, 'date': (2022, 2, 11)},
 {'author': 'Frank', 'comment': 'Python is fantastic', 'likes': 23, 'date': (2022, 2, 13)}
]

print(sorted(slownik, key=operator.itemgetter('likes')))


print(" ....................namedtuple")


Comment = namedtuple('Comment', ['author', 'content', 'likes', 'date'])

named_tuple_comment = [Comment('Alice', 'Python is powerful', 42, '(2022, 2, 3)'),
 Comment('Bob', 'Python is versatile', 17, '(2022, 2, 3)'),
 Comment('Charlie', 'Python is easy to learn', 91, '(2022, 2, 3)'),
 Comment('David', 'Python is super', 69, '(2022, 2, 3)'),
 Comment('Eva', 'Python is awesome', 55, '(2022, 2, 3)'),
 Comment('Frank', 'Python is fantastic', 23, '(2022, 2, 3)')]

from operator import attrgetter

print(sorted(named_tuple_comment,key=operator.itemgetter(2)))
print(sorted(named_tuple_comment,key=operator.attrgetter('likes')))

print(sorted(named_tuple_comment,key=operator.attrgetter('author')))
