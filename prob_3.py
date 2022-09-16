# Задайте список из вещественных чисел. Напишите программу которая надет разницу между максимальным и 
# минимальными значениями дробной части элементов
# пример: [1.1, 1.2, 3.1, 5, 10.01]=> 0.19

import random as rand


l1 = [1.1, 1.2, 3.1, 5, 10.01]
print(l1)
mx = l1[0]%1
mn = l1[0]%1
print(mx)
print(mn)
for i in range(1,len(l1)):    
    if l1[i]%1 > mx:
        mx = round(l1[i]%1, 3)
    if l1[i]%1 > 0 and l1[i]%1 < mn:
        mn = round(l1[i]%1 , 3)
    print(mx)
    print(mn)
    print('-' * 5)
print(f'min {mn}, max {mx}, max-min {round(mx - mn, 3)}')
