class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def birth(self):
        return "This creature has birth"

    def speak(self):
        ...


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        return "Woof!"

    def birth(self):
        return Animal.birth(self) + ' 24.04.2023'

    def swim(self):
        print("I can swim like a dog")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Meow!"

    def climb(self):
        print("I can climb")


if __name__ == '__main__':
    dog = Dog('Oscar')

    print(dog.speak())
    print(dog.birth())
    print(dog.get_name())
    dog.swim()

    cat = Cat('Felix')

    print(cat.speak())
    print(cat.birth())
    print(cat.get_name())
    cat.climb()

    print(Cat.__mro__)

