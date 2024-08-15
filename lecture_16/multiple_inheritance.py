
class Parent1:
    def method1(self):
        print('call method1 from Parent1')

    def common_method(self):
        print('common_method from Parent1')


class Parent2:
    def method2(self):
        print('call method2 from Parent2')

    def common_method(self):
        print('common_method from Parent2')


class Child(Parent1, Parent2):
    def common_method(self):
        Parent1.common_method(self)
        Parent2.common_method(self)


child = Child()
child.method1()
child.method2()
child.common_method()


print(Child.mro())


# Приклад: Доступ до змінних з однаковими іменами в різних прародичах
class Mama:
    common_field = "значення від Mama"

class Dad:
    common_field = "значення від Dad"

class Parent(Mama, Dad):
    pass

class Child(Parent):
    def access_common_field(self):
        common_field_from_mama = Mama.common_field  # Звертаємося до Grandparent1
        common_field_from_dad = Dad.common_field  # Звертаємося до Grandparent2
        print("Змінна common_field з Mama:", common_field_from_mama)
        print("Змінна common_field з Dad:", common_field_from_dad)

child = Child()
child.access_common_field()