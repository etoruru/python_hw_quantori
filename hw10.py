""" Гипотеза Коллатца
может быть кратко выражена следующим образом:

берём любое натуральное число n, если оно чётное,
то делим его на 2 если нечётное, то умножаем на 3
и прибавляем 1 (получаем 3n + 1) над полученным
числом выполняем те же самые действия, и так далее.

Гипотеза Коллатца заключается в том, что какое бы
начальное число n мы ни взяли, рано или поздно мы
получим единицу.

Пример
Для числа 12:
12
6
3
10
5
16
8
4
2
1
Всего получаем 9 шагов.

Задача
Вычислить число шагов для числа n, согласно гипотезе
Коллатца необходимых для достижения этим числом единицы. """
#!/usr/bin/env python3

num = int(input('Input a number: '))
steps = 0

while num != 1:
    if num % 2 == 0:
        num //= 2
        steps += 1
        print(num)
    else:
        num = 3 * num + 1
        steps += 1
        print(num)

print('steps = ', steps)

