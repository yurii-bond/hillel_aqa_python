from abc import ABC, abstractmethod


class NotAbstract(ABC):
    ...


not_abc = NotAbstract()
print(not_abc)


class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        ...

    def usual_method(self):
        print('Usual method')


class NewClass(AbstractClass):
    def abstract_method(self):
        print('Hello from NewClass')

NewClass().abstract_method()
NewClass().usual_method()


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        ...


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Tweet!"

def introduce(animal: Animal):
    print(f"My name is {animal.name} and I say {animal.make_sound()}")


dog = Dog("Buddy")
cat = Cat("Whiskas")
bird = Bird("Sparrow")

introduce(dog)
introduce(cat)
introduce(bird)

