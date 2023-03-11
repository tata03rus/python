# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного
# максимума)

N = int(input("Введите кол-во элементов в массиве: "))

import random
from random import randint
A = []
for i in range (N):
    A.append(randint(0, 100))
print(A)
min = int(input("Введите нижнюю границу диапазона: "))
max = int(input("Введите верхнюю границу диапазона: "))

B = list()
for i in range(N):
    if A[i] > min and A[i] < max:
        print ("Индекс {}: значение = {}".format(i, A[i]))