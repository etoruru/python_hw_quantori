#!/usr/bin/env python3

def letters_range(start, stop, step=1):
    return [chr(code) for code in range(ord(start), ord(stop), step)]

print(letters_range('p', 'g', -2))
