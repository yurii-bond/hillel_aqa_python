# __iter__() - повертає об'єкт ітератора
# __next__()

iter_list = [1, 2, 3, 4, 5]
print(iter_list) # [1, 2, 3, 4, 5]
iterable_obj = iter(iter_list)
print(iterable_obj) # ?

print(next(iterable_obj))
print(next(iterable_obj))
print(next(iterable_obj))
print(next(iterable_obj))
print(next(iterable_obj))
# print(iter_list[5], 'List')  -> IndexError: list index out of range
# print(next(iterable_obj), 'Iter object') -> StopIteration

for item in iter_list:
    print(item, ':from iter_list')


for i in iterable_obj:
    print('Hello')
    print(i, ':from iterable_obj')
else:
    print('Ok')


class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_num:
            self.current += 1
            return self.current
        else:
            raise StopIteration

my_iterator = MyIterator(5)
for i in my_iterator:
    print(i)

my_range = range(3, 6, 2)
my_range_iter = iter(my_range)
print(my_range_iter)
print(next(my_range_iter))
print(next(my_range_iter))
# print(next(my_range_iter))
# print(next(my_range_iter))
# print(next(my_range_iter))
# print(next(my_range_iter))
# print(next(my_range_iter))

for i in range(6):
    print(i, 'from range')