    # 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером
    # # 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
# symbol = {chr(i): i for i in range(32, 127) }
# i = 0
# for key,val in symbol.items():
#     i +=1
#     if i%10 == 0 and i != 0:
#         print()
#     print(f'{key}:{val}', end='   ')

for i in range(32, 128):
    print(f"({i}: {chr(i)})", end='  ')
    if i % 10 == 0:
        print()