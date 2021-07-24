# # 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# # Например, если введено число 3486, то надо вывести число 6843.

# def number_revers(num):
#     return num[::-1]
#
# print(number_revers(input("Введите число: ")))
num = ''
number = [i for i in input("Введите число: ")]

while len(number):
    num = num + number.pop()

print(num)