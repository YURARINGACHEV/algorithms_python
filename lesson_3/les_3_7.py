# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint
from random import randint
N = int(input("Введите количество чисел в списке "))
array = []
for i in range(N):
    array.append(randint(0, 19))
print(array)
min1 = min(array)
array.remove(min1)
min2 = min(array)
print(min1)
print(min2)