#Use the zip() function. This function takes two or more iterables (like list, dict, string),
# aggregates them in a tuple, and returns it.

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

d = zip(list1,list2)
print(list(d))
# print(tuple(d))

print(".........................nested list........")
#The given list is a nested list. Use indexing to locate the specified item,
# then use the append() method to add a new item after it.
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

print(list1[2])
print(list1[2][3])
print(list1[2][2][0])


print("..............Exercise 8: Extend nested list by adding the sublist..........................")
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]


print(list1[2][1][2])
list1[2][1][2] += sub_list
print(list1)

list1[2][1][2].extend(sub_list)
print(list1)


print("....................options to copy a list................")
aList = ['xyz', 'zara', 'PYnative']
newList = aList.copy()
print(newList)

newList2 = list(aList)
print(newList2)

