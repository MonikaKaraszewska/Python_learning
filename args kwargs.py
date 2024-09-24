def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3,5,6,7)) # wpisujemy na biezaco tyleilechcemy


#a bez args:
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3] #mamy liste konkretna zapissana
print(my_sum(list_of_integers))

# niemusinazywac sie args,moze miec inna nazwe np *integers,*dom * ta gwazdka to unpacking operator
def my_sum(*dom):
    result = 0
    for x in dom:
        result += x
    return result

print("*dom: ", my_sum(1, 2, 3,99))


def funkcja(*args):
    print("Ilosc zmiennych: ", len(args))
    for arg in args:
        print(arg)


funkcja(1, 2, "abc", [1, 2, 3])


def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for i in kwargs.values():
        result += i
    return result

print("**kwargs: ", concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))


list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print("Mys_sum: ", my_sum(*list1, *list2, *list3))

print("..............Unpacking With the Asterisk Operators: *...................")

my_list = [1, 2, 3]
print(my_list) # tu mamy w profmielisty wyswietlone
my_list = [1, 2, 3]
print(*my_list) # a tu rozpakowana liste, zawartosc wysiwetlona

print("......* operator works on any iterable object. It can also be used to unpack a string:")
a = [*"RealPython"]
print(a)


print(".......................split a list into three different parts. ..........")
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print(a)
print(b)
print(c)

print(".......................split a list an merge with secodn list ..........")


my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)


print(".......................merge two different dictionaries by using the unpacking operator **:")
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)

*a, = "RealPython"
print(a)
