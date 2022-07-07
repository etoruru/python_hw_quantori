""" Встроенная функция input позволяет ожидать и возвращать данные из стандартного
ввода ввиде строк (весь введенный пользователем текст до нажатия им enter).
Используя данную функцию, напишите программу, которая:

1. После запуска предлагает пользователю ввести целые неотрицательные числа,
разделенные любым не цифровым литералом (пробел, запятая, %, буква и т.д.).
2. Получив вводные данные, выделяет полученные числа, суммирует их,
и печатает полученную сумму.

Например:

-> 12 12 12
36

-> 123dfgdr%0&45ty-45--900
-777 """
#!/usr/bin/env python3
from functools import reduce


TERM = "\n"

def sym_to_state(sym):

    if sym in "0123456789":
        return "digit"

    elif sym == "-":
        return "minus"

    elif sym == TERM:
        return "term"

    else:
        return "other"


def task(line):

    line += TERM

    num_list = []
    num_current = ""

    state = None

    for sym in line:

        state_new = sym_to_state(sym)

        transition = (state, state_new)

        state = state_new

        if transition == (None, "digit"):
            num_current += sym

        elif transition == ("digit", "digit"):
            num_current += sym

        elif transition == ("minus", "digit"):
            num_current += "-"
            num_current += sym

        elif transition == ("other", "digit"):
            num_current += sym

        # commitment

        elif transition == ("digit", "other"):
            num_list.append(num_current)
            num_current = ""

        elif transition == ("digit", "minus"):
            num_list.append(num_current)
            num_current = ""

        elif transition == ("digit", "term"):
            num_list.append(num_current)
            num_current = ""

    return num_list


if __name__ == "__main__":
    text = input('Введите строку: ')
    summa = reduce(lambda x,y: x + y, [int(num) for num in task(text)])
    print(summa)
