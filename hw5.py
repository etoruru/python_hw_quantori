#!/usr/bin/env python3

s = input()

num_lst = s.split(' ')

lst = [int(num) for num in list(set(num_lst))]
lst.sort()

i = 0
while i < len(lst) - 1: 
    if lst[i + 1] == lst[i] + 1 :
        i += 1
    else:
        print(lst[i] + 1)
        break
else:
    print(lst[i] + 1)
