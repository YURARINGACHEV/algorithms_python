
import sys
# # 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# # выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
#
n = int(input("Введите любое натуральное число: "))
list_n = sum([i for i in range(1, n+1)]) == n * (n + 1)/2
print(list_n)
    
print(f'Размер натурального числа, {sys.getsizeof(n)}')
print(f'Размер спика: {sys.getsizeof(list_n)}')
sum = sys.getsizeof(n) + sys.getsizeof(list_n)
print(f'Сумма: {sum}')