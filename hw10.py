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

