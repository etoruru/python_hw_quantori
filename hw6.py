""" 

https://projecteuler.net/problem=36

The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2. (Please note that the palindromic number,
in either base, may not include leading zeros.)

Напишите программу, которая решает описанную выше задачу и печатает ответ. """
#!/usr/bin/env python3

sum = 0

def isPalindrome(num, base):
    reverse = 0
    temp = num
    while temp > 0:
        reverse = reverse * base + temp % base
        temp = int(temp / base)
    return reverse == num

for i in range(1000000):
    if isPalindrome(i, 10):
        if isPalindrome(i, 2):
            sum += i

print(sum)


