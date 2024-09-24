# def gen():
#     i = 0
#     while i < 5:
#         yield i
#         i += 1
# print(list(gen()))
#
# for i in gen():
#     print(i)

#

def parzyste(x):
    i=0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1

print(list(parzyste(30))) # albo przez pentle for

# for i in parzyste(16):
#     print(i)

