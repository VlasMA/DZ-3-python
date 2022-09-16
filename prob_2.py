# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

num = int(input('Введите число: '))

def fib(num):
    numbers = []
    a, b = 1, 1
    for i in range(num-1):
        numbers.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (num):
        numbers.insert(0, a)
        a, b = b, a - b
    return numbers

numbers = fib(num)
print(fib(num))
print(numbers.index(0))