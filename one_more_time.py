number_of_people = 3
suma = 0
min_age = 100
max_age=0
for i in range(1,number_of_people+1):
    age = int(input(f"podaj wiek nr {i}: "))
    suma+=age
    if age <min_age:
        min_age = age
    else:
        max_age = age
print("sredni wiek to: ", suma/number_of_people)
print('max: ', max_age)
print("min: ", min_age)