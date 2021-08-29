#!/usr/bin/env python3

import pickle


f = open('newfile.py', 'rb')
obj = pickle.load(f)

print(obj)
