# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

nam = int(input("input namber: "))
my_list = []

for i in range(nam):
    my_list.append((-3)**i)

print(f'Для N = {nam}:', end = ' ')
print(*my_list, sep = ', ')
 