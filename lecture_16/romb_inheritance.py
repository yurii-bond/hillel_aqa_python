         #      Animal
         #      /   \
         # Mammal   Bird
         #      \   /
         #       Bat


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass  # Абстрактний метод

class Mammal(Animal):
    def __init__(self, name, num_legs):
        Animal.__init__(self, name=name)
        self.num_legs = num_legs

class Bird(Animal):
    def __init__(self, name, wingspan):
        Animal.__init__(self, name=name)
        self.wingspan = wingspan

class Bat(Mammal, Bird):  # Ромбовидне наслідування
    def __init__(self, name, num_legs, wingspan):
        Mammal.__init__(self, name=name, num_legs=num_legs)
        Bird.__init__(self, name=name, wingspan=wingspan)

    def sound(self):
        return "Squeak"  # Звук кажана

# Створення об'єкту класу Bat
bat = Bat("Bat", 2, 30)

# Виведення атрибутів об'єкту bat
print("Назва:", bat.name)
print("Кількість ніг:", bat.num_legs)
print("Розмах крил:", bat.wingspan)

# Виклик методу sound для об'єкту bat
print("Звук:", bat.sound())

print(Bat.mro())