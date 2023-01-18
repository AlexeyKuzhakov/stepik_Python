# Списки

students = ['Ivan', 'Masha', 'Sasha']
students2 = ['Dasha', 'Oleg']

students[1] = 'Sergey'
print(students)

students3 = students + students2
print(students3)

students3.append('Alexey')
students3 += ['Kseniya']
students3.insert(1, 'Gena')
print(students3)

for student in students3:
    print(f'Hello, {student}!')

students3.remove('Sasha') #Удаляет элемент из списка по первому вхождению
del students3[1]  #Удаляет элемент из списка по индексу
print(students3)

if 'Oleg' in students3:     #Проверка есть ли элемент в списке
    print('Oleg is here')

ind = students3.index('Oleg')   #Возвращяет позицию элемента в списке
print(ind)

ordered_students = sorted(students3)    #Выводит элементы списка по алфавиту, но не меняет сам список
print(ordered_students)

students3.sort()
print(students3)    #Сортирует список по алфавиту, если список цифр то по возростанию


# Генерация списков

a = [0]*5
print(a)

a = [0 for i in range(5)]
print(a)

a = [i * i for i in range(5)]
print(a)

a = [int(i) for i in input('Введите числа через пробел: ').split()]
print(a)


# Двумерные списки

n = 3
a = [[0] * n for i in range(n)]
print(a)
a = [[0 for j in range(n)] for i in range(n)]
print(' '.join(map(str, a)))


# Поиск минимума в списке

a = [int(i) for i in input().split()]
m = a[0]
for x in a:
    if m > x:
        m = x
print(m)