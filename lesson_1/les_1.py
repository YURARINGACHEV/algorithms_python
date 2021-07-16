# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

def sum_composition_three(number):
    sum_number = 0
    composition_number = 1
    if len(number) == 3:
        for i in number:
            sum_number = sum_number + int(i)
            if int(i) != 0:
                composition_number = composition_number * int(i)
    return sum_number, composition_number

sum_number, composition_number = sum_composition_three(input("Введите число "))
print(sum_number, composition_number)
