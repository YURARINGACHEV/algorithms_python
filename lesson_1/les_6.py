# Пользователь вводит номер буквы в алфавите. Определить, какая это буква
def number_letter(first, last):
    alf_list = [chr(i) for i in range(ord(first), ord(last)+1)]
    alf_dict = {i: j for i,j in zip(range(1, len(alf_list)+1), ''.join(alf_list),  )}
    return alf_dict
alf_diсt = number_letter(input("Введите первую букву алфавита: "), input("Введите последнюю букву того же алфавита: "))
print(alf_diсt)
number = int(input('Введите номер буквы от 0 до 32: ' ))
if number > len(alf_diсt) or number <= 0:
    print("Ваш номер не входит в диапазон списка алфавита: ")
else:
    print(f"Ваша буква '{alf_diсt[number]}'")