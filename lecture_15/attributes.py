import math

class Car(object):
    speed = 0
    __quantity = 0

    # Конструктор
    def __init__(self):
        Car.__quantity += 1

    def start_engine(self):
        """

        :return:
        """
        return 'Engine started'

    def get_speed(self):
        return Car.speed

    def get_quantity(self):
        return Car.__quantity

    # Деструктор
    def __del__(self):
        Car.__quantity -= 1


my_car = Car()
print(my_car.speed)
print(my_car.start_engine())
print(my_car.get_quantity(), 'quantity')

my_another_car = Car()
print(my_car.get_quantity(), 'quantity')
my_car.speed = 30

print(my_car.speed)
my_car.wheels = 4
print(my_car.wheels, 'wheels')
print(my_another_car.speed)
my_another_car.speed = 50
print(my_car.speed)
print(my_another_car.speed)
Car.speed = 45
print(my_car.get_speed())
print(my_another_car.get_speed())

var = 0
print(var, 'var')

del my_another_car

print(my_car.get_quantity(), 'quantity')
