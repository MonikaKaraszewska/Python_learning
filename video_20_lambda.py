#lambda = funkcje anonimowe
def kwadrat(x):
    return x * x

print(kwadrat(5))

wynik = (lambda x: x*x)(3)
print("wynik: ", wynik)

suma= (lambda y,z:z+y)(3,5)
print("suma: ", suma)

lam2 = lambda m,b,c: m + b * c
print("lam2: ", lam2(3,4,2))


lam = lambda x: x*x
print(lam(2))
print(lam(9))
print('')
print('video 4 Python Tutorials ......lambda function............PyMoodra')

lambda_sum = lambda x,y : x+y
print("lambda_sum: ",lambda_sum(3,4))

def get_sum(x,y):
    return x+y

# w lambda zamiats np(x+y) mozemy podac funkcje

lambda_sum2 = lambda x,y: get_sum(x,y)
print("lambda_sum2: ", lambda_sum2(3,4))

lambda_sum3 = lambda x,y: get_sum(x,y) + get_sum(x,y)
print("lambda_sum3: ", lambda_sum3(3,4))

print("lambda to funkcja:", type(lambda_sum3))
print(' ')
print('...............................................*args  with unknown arguments')
x= lambda *args : sum(args)
print(x(2,3,4,5))

print(' ')
print('..............................................conditional statemnts')
y = lambda x,y: x if x>y else y
print(y(5,8))