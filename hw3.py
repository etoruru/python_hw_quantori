#!/usr/bin/env python3

s = input('Введите текст: ')

str_lcase = s.lower()
word_lst = str_lcase.split(' ')

words_dict = {word: word_lst.count(word) for word in set(word_lst)}

maximum = max(list(words_dict.values()))

for key, value in words_dict.items():
    if value == maximum:
        print(str(value) + ' - ' + key)



