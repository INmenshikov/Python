# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [2, 3, 5, 9, 3]
list_odd = lst[1::2]
print(list_odd)
sum_list_odd = sum(list_odd)
# Вывод как в примере
print(f'{lst} -> на нечётных позициях элементы', end = ' ') 
print(*list_odd, end = '', sep =' и ')
print(f', ответ: {sum_list_odd}')
# Вывод как надо
print(f'{lst} -> на нечётных позициях элементы', end = ' ') 
print(*list_odd, end = '', sep =', ')
print(f'. Ответ: {sum_list_odd}')
