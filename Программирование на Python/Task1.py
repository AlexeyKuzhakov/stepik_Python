# Требуется определить, является ли данный год високосным.
# Напомним, что високосными годами считаются те годы, порядковый номер которых либо кратен 4,
# но при этом не кратен 100, либо кратен 400 (например, 2000-й год являлся високосным, а 2100-й будет невисокосным годом).
# Программа должна корректно работать на числах 1900≤n≤3000.
# Выведите "Високосный" в случае, если считанный год является високосным и "Обычный" в обратном случае

a = int(input('Введите код: '))
if a % 400==0 or a % 4==0 and a % 100 != 0:
    print('Високосный')
else:
    print('Обычный')