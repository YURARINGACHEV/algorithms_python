# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
n = int(input('Введите количество элементов последовательности: '))
s = 0

for i in range(n):
    s += (-1 / 2) ** i

print(f'Сумма {n} чисел последовательности = {s}')