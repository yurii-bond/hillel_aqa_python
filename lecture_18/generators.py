def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


fib = fibonacci_generator()
print(fib)
for _ in range(11):
    print(next(fib))

def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))