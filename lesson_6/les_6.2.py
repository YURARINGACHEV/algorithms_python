import sys

# # 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# # Например, если введено число 3486, то надо вывести число 6843.

num = ''
number = [i for i in input("Введите число: ")]
number_list = number
num1 = sys.getsizeof(number[0])

while len(number):
    num = num + number.pop()

print(num)

print(f'Размер num, {sys.getsizeof(num)}')
print(f'Размер спика number: {sys.getsizeof(number)}')
print(f'Размер элемента спика number: {num1}')
sum = sys.getsizeof(num) + sys.getsizeof(number) + num1
print(f'Сумма равна {sum}')

#
# Введите число: 123
# 321
# Размер num, 28
# Размер спика number: 28
# Размер элемента спика number: 26
# Общая память: 82

print(f"Общая память: {sum}")
