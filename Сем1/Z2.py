# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90
my_list = []
while True:
    namber = input("Введите число: ")
    if namber == '':
        break
    my_list.append(int(namber))
print(my_list)
max = my_list[0]
i = 0
while i < len(my_list):
    if my_list[i] > max:
        max = my_list[i]
    i += 1
print(f'мах = {max}')

exit()
n1 = int(input('Введите число: '))
n2 = int(input('Введите число: '))
n3 = int(input('Введите число: '))
n4 = int(input('Введите число: '))
n5 = int(input('Введите число: '))

a = [n1 , n2 , n3 , n4 , n5]
max = a[0]
i = 0
while i < len(a):
    if a[i] > max:
        max = a[i]
    i += 1
print(f'мах = {max}')
