# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
# 1−(x+2)^2 при x≤−2
# -x/2 при −2<x≤2
# (x-2)^2+1 при 2<x
# Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.


def f(x):
    if x <= -2:
        f = 1 - (x + 2)**2
    elif -2 < x <= 2:
        f = (-x) / 2
    elif x > 2:
        f = (x - 2)**2 + 1
    return f

print(f(x))