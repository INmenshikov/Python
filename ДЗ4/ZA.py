# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]
import random
exponent = int(input("Задайте натуральную степень: ")) 
print(f'k = {exponent}, то многочлены могут быть => ', end = '')
if exponent == 0: print("Задайте натуральную степень отличную от нуля!" )
else: 
    i = 0 
    while exponent > 0:
        if i == 0:
            r_namber = random.randint(-100,100)
            while r_namber == 0:
                r_namber = random.randint(-100,100)
            i += 1
        else: r_namber = random.randint(-100,100) 
        if r_namber > 0:
            print(r_namber, end = '')
            print(f'*x**{exponent}',end = '')
            if exponent > 1:
                print(' + ',end = '')
            exponent -= 1
        elif r_namber == 0:
            exponent -= 1
            continue
        else:
            print(r_namber * (-1), end = '')
            print(f'*x**{exponent}',end = '')
            if exponent > 1:
                print(' + ',end = '')
            exponent -= 1
print(" = 0")