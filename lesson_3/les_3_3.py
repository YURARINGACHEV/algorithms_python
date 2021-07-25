# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint
N = int(input("Введите количество чисел в списке "))
arr = []
for i in range(N):
    arr.append(randint(0, 19))
print(arr)
index_min = arr.index(min(arr))
index_max = arr.index(max(arr))
arr[index_min],arr[index_max] = arr[index_max],arr[index_min]
print(arr)
