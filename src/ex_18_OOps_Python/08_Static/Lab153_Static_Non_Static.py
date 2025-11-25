class MathOperation:

    def div(self, a, b):
        return a / b

    @staticmethod
    def sum(a, b):
        return a + b


t = MathOperation()
print(t.div(10, 10))

#print(MathOperation.div(10, 10)) #as this os not statis method we have to call it using oblect
print(MathOperation.sum(10, 10))