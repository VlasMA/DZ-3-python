# Задайте список из нескольких чисел. напишите программу,
# которая найдет сумму элементов списка стоящик на нечетных позициях.
# Пример: [2, 3, 5, 9, 3] на нечетных позициях элементы 3 и 9. Ответ 12

from random import randint

l1 = []
s = 0
n = int(input('Укажите размер списка :'))
for i in range(n):
    l1.append(randint(-50, 50))
print(l1)
for i in range(len(l1)):
    if i%2 == 1:
        s += l1[i]
print(s)