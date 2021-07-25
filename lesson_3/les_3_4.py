# Определить, какое число в массиве встречается чаще всего.
from random import randint
N = int(input("Введите количество чисел в списке "))
arr = []
for i in range(N):
    arr.append(randint(0, 19))
print(arr)

num = arr[0]
max_num = 1
for i in range(N - 1):
    num = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            num += 1
    if num > max_num:
        max_num= num
        ans_num = arr[i]

if max_num > 1:
    print(max_num, 'раз(а) встречается число', ans_num)
else:
    print('Все элементы уникальны')