# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
def average_number(a, b, c):
        if a > b > c or c > b > a:
                return f"Среднее число b =  {b}"
        elif b > a > c or c > a > b:
                return f'Среднее число a =  {a}'
        elif a > c > b:
                return f"Среднее число с = {c}"
        return "Введите разные числа"

a, b, c = map(int, input("Введите три разных числа a, b, c: ").split())
print(average_number(a, b, c))