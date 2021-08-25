#!/usr/bin/env python3 
from functools import reduce

# problem 6
summa = sum([i for i in range(1, 101)]) ** 2 - sum((i ** 2 for i in range(1, 101)))
#print(summa)

# problem 9
a, b, c = [tupl for tupl in [(a, b, 1000 - a - b) for a in range(1, 1000 // 3) for b in range(1, 1000 // 2)] if tupl[0] ** 2 + tupl[1] ** 2 == tupl[2] ** 2 and sum(tupl) == 1000][0]
#print(a*b*c)

# problem 40
print(reduce(lambda x,y: x*y,  [int(''.join([str(i) for i in range(1, 100000)])[10 ** i-1]) for i in range(6)]))


# problem 48
last_digits = str(sum([i ** i for i in range(1,1001)]))[len(str(sum([i ** i for i in range(1,1001)])))-10:]
#print(last_digits)    
