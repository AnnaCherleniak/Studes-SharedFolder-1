# 3. Создайте функцию генератор чисел Фибоначчи

def func_fibonacci(number):
    a, b = 0, 1
    yield a
    count = 0
    while count < number:
        count += 1
        a, b = b, a + b
        yield a


print(*list(func_fibonacci(10)))
