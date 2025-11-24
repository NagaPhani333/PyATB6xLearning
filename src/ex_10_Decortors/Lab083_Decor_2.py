def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
        print('tst')
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
        print('test')
    return wrapper


@decorator1
@decorator2
def say_hello():
    print("Hello!")


say_hello()