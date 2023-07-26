value1 = input('Digite um valor: ')
value2 = input('Digite outro valor: ')

if value1 > value2:
    print(f'{value1=} é maior do que {value2=}')
elif value2 > value1:
    print(f'{value2=} é maior do que {value1=}')
else:
    print('Os valores são iguais')