print('Привет мир')
name = input('Ваше имя: ')
print(f'Привет {name}')

print('1', '2', '3', sep='&')   # В параметре sep указывается разделитель

print('1', '2', end='/')    # Если перенос строки не нужен, либо нужен явный разделитель, исполдьуется параметр end
print('3', '4')
# Значения по умолчанию: sep = ' '  end = '\n'

