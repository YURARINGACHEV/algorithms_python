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
