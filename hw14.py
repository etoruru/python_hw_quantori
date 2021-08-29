#!/usr/bin/env python3
# чтобы проверить, что записалось в файл, нужно запустить hw14_1.py

from Employee import Employee
import pickle


mary = Employee('Mary', '89102344411')
f = open('newfile.py', 'wb')
pickle.dump(mary, f)
f.close()


