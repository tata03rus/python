# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1


N = int(input("Введите кол-во элементов в массиве: "))
import random
from random import randint
A = []
for i in range (N):
    A.append(randint(0, 5))
print(A)

X = int(input("Введите число: "))
result = {}
for i in A:
    result[i] = result.get(i,0) + 1

print(result[X])

