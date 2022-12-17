# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int
import random
def generating_sheet_random_numbers(a,b,c):
    lst = []
    for i in range(c):
        lst.append(random.randint(a,b))
    return lst

def generating_bunch_random_number(a,b,c):
    bun = set()
    while len(bun) < c:
        g = random.randint(a,b)
        print(g)
        bun.add(g)     
    return bun

len_list = int(input('Введите длинну списка: '))
my_list = generating_sheet_random_numbers(0,99,len_list)
print(my_list)
i = 0
end_list = []
while i < len_list:
    ri = random.randint(0,len(my_list)-1)
    end_list.append(my_list[ri])
    my_list.pop(ri)
    ri = None
    i += 1
print(end_list)






