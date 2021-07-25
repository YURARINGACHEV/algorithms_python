# . В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint
N = int(input("Введите количество чисел в списке "))
arr = []
for i in range(N):
    arr.append(randint(0, 19) * -1)
print(arr)

i = 0
index = -1
while i < N:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(index + 1, ':', arr[index])