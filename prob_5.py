# Напишите программу которая найдет произведение пар чисел списка. Парой считается первый и последний элемент,
# второй и предпоследний
# [2,3,4,5,6]=> [12, 15, 16]

from random import randint




l1 = []
l2 = []
n = int(input('Укажите размер списка :'))
for i in range(n):
    l1.append(randint(2, 10))
print(l1)
for i in range((len(l1)+1)//2):
    # print(f'{l1[i]} * {l1[0-1-i]}')
    c = l1[i] * l1[0-1-i]
    l2.append(c)
print(l2)
