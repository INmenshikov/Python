# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import controller

controller.create_file(2,2)
a = open('./ДЗ4/file_1.txt', 'r')
str_a = ''
for i in a:
    str_a += i       
b = (open('./ДЗ4/file_2.txt', 'r'))
str_b = ''
for i in b:
    str_b += i
print(str_a)

print(str_b)
