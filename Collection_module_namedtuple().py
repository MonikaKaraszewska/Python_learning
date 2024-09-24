
from collections import namedtuple

Point = namedtuple("Point", "x y z gh") # string
Pointt = namedtuple("Pointt", ['x', 'y', 'z', 'gh']) # lista
PointDict = namedtuple("PointDict", {'f' :0, 'c' :5, 'a' :77, 'sz' :99}) # slownik - zignoruje wartosci i do kluczy przypisze nowe wartosci podane

print("....string")
newP = Point(3,4,5,9)
print(newP.x, newP.y)
print(newP[0])
p4 = newP._make(['a', 'b', 'b', 'p'])
print(p4)

print("....lista")
newPo = Pointt(9,8,7,6)
print(newPo.gh)
print(newPo[2])
p3 = newPo._make(['a', 'b', 'b', 'p'])
print(p3)

print("......slownik")
newD = PointDict(9,8,7,6)
print(newD.f)
print(newD[1])
print(newD._asdict())
print(newD._fields)
print(newD)
newDD = newD._replace(f=6)
print(newDD)

p2 = newD._make(['a', 'b', 'b', 'p'])
print(p2)