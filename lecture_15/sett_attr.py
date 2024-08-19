class Person:
    """
    Class Person with settattr method
    """
    def __setattr__(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """
        print(f'Setting {key} to {value}')
        super().__setattr__(key, value)

if __name__ == '__main__':


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

    if hasattr(person, 'zip_code'):
        print(person.zip_code)
    else:
        print("class Person doesn't have attribute 'zip_code'")


    setattr(person, 'zip_code', '90210')
    print(person.zip_code)
    delattr(person, 'zip_code')
    print(person.zip_code)