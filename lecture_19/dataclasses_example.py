from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    name: str
    age: int
    sort_index: int = field(init=False, repr=False)
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.age)


person1 = Person('Gerald', 30, 99)
person2 = Person('Yennifer', 25)
person3 = Person('Yennifer', 25)

print(id(person2), 'person2')
print(id(person3), 'person3')
print(person1, 'person1')

print(person2 == person3, 'person2==person3')
print(person1 > person3, 'person1 > person3')


