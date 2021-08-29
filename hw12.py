#!/usr/bin/env python3

def fib(n):
    prev, cur = 0, 1
    seq = []
    seq.append(cur)
    for i in range(2, n + 1):
        prev, cur = cur, prev + cur
        seq.append(cur)
    return seq

s = fib(5432)
print(s[-1])
        
