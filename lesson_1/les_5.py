# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
def number_letter(first, last):
    alf_list = [chr(i) for i in range(ord(first), ord(last)+1)]
    alf_dict = {i: j for i,j in zip(''.join(alf_list), range(1, len(alf_list)+1))}
    return alf_dict

def find_letter(a, b, alf_dict):
    count_letters = 0
    print(f'Место буквы {a}:  {alf_dict[a]}')
    print(f'Место буквы {b}:  {alf_dict[b]}')
    first_letter = len(alf_dict) - alf_dict[a]
    second_letter = len(alf_dict) - alf_dict[b]
    if alf_dict[a] < alf_dict[b]:
        count_letters = first_letter - second_letter - 1
    elif alf_dict[b] < alf_dict[a]:
        count_letters = second_letter - first_letter - 1
    else:
        print("Вы ввели одинаковые буквы")
    print(f'Букв находится: {count_letters}')

alf_diсt = number_letter(input("Введите первую букву алфавита: "), input("Введите последнюю букву того же алфавита: "))
print(alf_diсt)
find_letter(input("Введите первую букву: "), input("Введите вторую букву: "), alf_diсt)

