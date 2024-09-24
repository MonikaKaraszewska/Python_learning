class Dog:

    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    '''the underscore (_) is used as a throwaway variable, indicating that 
        its value is not going to be used in the loop body. Pętla będzie powtarzać 
        operację printowania "Bark!" dokładnie n razy, niezależnie od wartości samego _.
        _ jest jedynie zmienną tymczasową, która jest ignorowana w ciele pętli. Ważne jest, 
        ile razy pętla zostanie wykonana, co jest określone przez wartość n.'''

    @staticmethod
    def nbark(n):
        """barks n times"""

        for _ in range(n):
                print("Bark!")


tony = Dog('Tony')
tim = Dog('Tim')

print(tony.name)

print('...........')
print("1:", Dog.num_dogs())
tony.nbark(5)
print(tony.num_dogs())
Dog.nbark(4)