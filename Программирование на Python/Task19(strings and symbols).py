# Проверить является ли строка палиндромом

s = input()
r = s[::-1]

if s == r:
    print('Yes')
else:
    print('No')