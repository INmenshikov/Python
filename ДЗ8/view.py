
def imput_class():
    return input('С каким классом работаем? ').upper() # верхний регистор

def input_subject():
    return input('Какой предмет? ').lower()

def who_answer():
    return input('Кто будет отвечать? ')

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')

def what_mark():
    return input('На какую оценку ответил? ')
