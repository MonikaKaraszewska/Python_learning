lista = ["mama", "tata", "asia", "krolik"]
num = [1, 2,34,5,6,7]

newlista = list(map(lambda i: i.upper, lista))
print(newlista)

replace_a = lambda word: ''.join('#' if char == 'a' else char for char in word)

# Użycie funkcji map do zastosowania funkcji replace_a dla każdego słowa w liście
new_lista = list(map(replace_a, lista))

# Wydrukowanie wyniku
print(new_lista)

print(list(zip(num,lista)))