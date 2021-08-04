import sys
# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
number = input("Введите число ")
number_even = []
number_odd = []
for i in number:
    if int(i)%2 == 0:
        number_even.append(i)
    else:
        number_odd.append(i)
print(f"Четные числа {' '.join(number_even)} в количестве {len(number_even)} " )
print(f"Нечетные числа {' '.join(number_odd)} в количестве {len(number_odd)} ")

print(f"Байт памяти для number: {sys.getsizeof(number)}")
print(f"Байт памяти для number_even: {sys.getsizeof(number_even)}")
print(f"Байт памяти для number_odd: {sys.getsizeof(number_odd)}")
sum_member = sys.getsizeof(number) + sys.getsizeof(number_even) + sys.getsizeof(number_odd)
print(f'В программе задействовано байт памяти: {sum_member}')

# Введите число 123456
# Четные числа 2 4 6 в количестве 3
# Нечетные числа 1 3 5 в количестве 3
# Байт памяти для number: 31
# Байт памяти для number_even: 44
# Байт памяти для number_odd: 44
# В программе задействовано байт памяти: 119