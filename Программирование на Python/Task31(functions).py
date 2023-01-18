# Функция поиска минимума из произвольного кол-ва чисел
def minim(*a):
    m = a[0]
    for x in a:
        if m > x:
            m = x
    return m

print(minim(4, 2, 6, 12, 5))


# Функция range с выводом списка
def my_range(start, stop, step=1):
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
    return res

print(my_range(1, 14, 3))

