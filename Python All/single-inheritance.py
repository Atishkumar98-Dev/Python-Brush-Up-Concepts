class Parent:
    def method(self):
        print("Parent method")

class Child(Parent):
    pass

c = Child()
c.method()