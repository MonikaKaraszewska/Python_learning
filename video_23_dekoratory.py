def decorator(func):
    def wrapper():
        print("--------------")
        func()
        print("--------------")
    return wrapper

def hello():
    print("hello World")

hello = decorator(hello)
hello()

@decorator
def witaj():
    print("witaj swiecie")

witaj()