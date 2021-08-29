#!/usr/bin/env python3

def convert_CtoF(deg):
    return (deg * 1.8) + 32


def convert_FtoC(deg):
    return (deg - 32) * (5 / 9)


def convert(deg, mode):
    try:
        deg = float(deg)
    except ValueError:
        return 'Значение должно быть числом или десятичным числом, разделенное "." '
    if mode == 1:
        return convert_CtoF(deg)
    elif mode == 2:
        return convert_FtoC(deg)
    else:
        return 'Введен некорректный режим!'


if __name__ == '__main__':
    mode = int(input('Выберите режим:\n 1 - C перевести в F \n 2 - F перевести в С\n'))
    deg = input('Введите значение: ')
    res = convert(deg, mode)
    print(res)


    
