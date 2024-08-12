from inspect import stack


class MagicMethods:
    # Конструктор
    def __init__(self, magic='This is magic!'):
        self.magic = magic

    def __len__(self):
        return len(self.magic)

    def __add__(self, other):
        return self.magic + " " + other.magic

class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def __len__(self):
        return len(self.__items)


magic_one = MagicMethods()
magic_two = MagicMethods('This is another magic!')

print(len(magic_one))
print(len(magic_two))

print(magic_one.__add__(magic_two))

_stack = Stack()
_stack.push(1)
_stack.push('abc')
print(len(_stack), "stack length")