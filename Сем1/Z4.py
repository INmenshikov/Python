# 2. Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3
namber = input('input namber: ')
namber = namber.split('.')
if len(namber) < 2: print("Целое")
else: print(namber[1][0])
exit()
a = float(input("input namber: "))
b = (a * 10) % 10
if a - round(a) == 0: # round - округлеине
    print('not')
else: print(int(b))

