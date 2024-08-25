class Parent1:
    def method1(self):
        print("Parent1 method")

class Parent2:
    def method2(self):
        print("Parent2 method")

class Child(Parent1, Parent2):
    pass

c = Child()
c.method1()  # Output: Parent1 method
c.method2()