# global_var = 1


class DemoClass:
    variable = 0

    def print_var(self):
        print(global_var)


DemoClass.variable


def func():
    global global_var
    global_var = 3
    print(global_var)


# print(global_var) #  1
func() #  3
print(global_var) # 3


def func2():
    z = 30
    def func3():
        nonlocal z
        z = 40
        print(z)
    func3()
    return z

print(func2())
