from oop_inheritance import Animal, Dog, Cat


def make_sound(animal):
    if isinstance(animal, Animal):
        print(animal.speak())
    else:
        raise TypeError("This not an instance of the Animal class")


if __name__ == '__main__':
    dog = Dog('Oscar')
    cat = Cat('Felix')
    creature = 'Pibodi'
    make_sound(dog)
    make_sound(cat)
    make_sound(creature)
