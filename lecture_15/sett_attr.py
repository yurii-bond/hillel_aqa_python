class Person:
    def __setattr__(self, key, value):
        print(f'Setting {key} to {value}')
        super().__setattr__(key, value)


person = Person()

setattr(person, 'name', 'Alice')
setattr(person, 'age', 30)

print(person.name)
print(person.age)

person.age = 35

print(person.age)

setattr(person, 'name', 'Aniston')

print(person.name)

person.address = 'New York'
print(person.address)