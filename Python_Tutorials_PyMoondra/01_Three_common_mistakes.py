def create_numer_list(numbers_range):
    numbers = []
    for i in range(numbers_range):
        if i not in numbers:
            numbers.append(i)
    return numbers


print(create_numer_list(3))

grocery_list = ['apple ', " Banana", " carrot ", 'eggplant']

for i in grocery_list:
    i = i.lower().strip()
    print(i)

