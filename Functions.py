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
        bun.add(str(g))   
    return bun

my_list = generating_bunch_random_number(0,10,10)
my_list.add(45)
print(my_list)