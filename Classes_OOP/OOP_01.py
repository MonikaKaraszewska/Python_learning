'''https://www.youtube.com/playlist?list=PLR-r0edywujedM6cbbrvWec18K6Rdk9W1'''
import statistics

'''method is function which is part of an object'''

''''properties = atribuites = instance variable = field'''


class NumberList(list):
    def __init__(self, *numbers):
        super().__init__(numbers)
        # self.length = len(numbers)
    def mean(self):
        return statistics.mean(self)
    @property
    def length(self):
        return len(self)


fibo = NumberList(1,2,3,4,5)
print(type(fibo))


print("mean: ", fibo.mean())
print("length: ",fibo.length)

for i in fibo:
    print(i)