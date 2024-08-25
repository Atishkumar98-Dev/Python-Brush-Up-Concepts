class MyClass:
    def __init__(self):
        self.__private = "priva9te"  # Private variable

    def get_private(self):
        return self.__private

obj = MyClass()
print(obj.get_private())  # Output: private
print(obj._MyClass__private)  # This is the correct way to access the private variable
