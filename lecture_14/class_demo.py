class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Car brand: {self.brand} and model: {self.model}"

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model


car = Car(brand='Toyota', model='Camry')
car2 = Car(brand='Toyota', model='Camry')
print(car.brand)
print(car.model)

print(car)
print(id(car))
print(type(car))
print(car2)
print(id(car2))
print(type(car2))

print(car == car2, "Using == method")
print(car.__eq__(car2), "Using __eq__ method")
print(car.model == car2.model)
print(car.brand == car2.brand)


