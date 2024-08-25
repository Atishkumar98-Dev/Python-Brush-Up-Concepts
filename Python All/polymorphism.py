class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

def make_sound(animal):
    print(animal.speak())

make_sound(Dog())  # Output: Woof
make_sound(Cat()) 