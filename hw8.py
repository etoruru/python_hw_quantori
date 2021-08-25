#!/usr/bin/env python3


def convert(num):
    if len(num) == 1:
        return int(num)
    else:
        return  int(num[0]) * (10 **(len(num)-1))  + convert(num[1:]) 


text = input('Введите текст: ')
while text != 'cancel':
    if text.isdigit():
        num = convert(text)
        if num % 2 == 0:
            print(num // 2)
            text = input()
        else:
            num = num * 3 + 1
            print(num)
            text = input()
    else:
        print('Не удалось преобразовать введенный текст в число.')
        break
else:
    print('Bye!')
