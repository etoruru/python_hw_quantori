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


