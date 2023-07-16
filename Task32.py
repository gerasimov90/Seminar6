# Задача 32: Определить индексы элементов массива 
# (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не 
# больше заданного максимума)
import random
list_1 = []
m = 10
for i in range(m):
    list_1.append(random.randint(0,100))
print('Дан массив чисел', list_1)
list_2 = []
max = int(input("Введите верхнюю границу диапазона max: "))
min = int(input("Введите нижнюю границу диапазона min: "))
for i in range(len(list_1)-1):
    if list_1[i] > min and list_1[i] < max:
        list_2.append(i)
print(list_2)