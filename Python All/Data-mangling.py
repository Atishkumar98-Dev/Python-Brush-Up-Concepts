class MyClass:
    def __init__(self):
        self.__private = "private"

obj = MyClass()
print(obj._MyClass__private)