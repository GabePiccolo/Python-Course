""" Calculadora com While """

while True:

    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+-/*): ')

    num_validos = None

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        num_validos = True
    except:
        print('erro)')
        num_validos = None

    if num_validos is None:
        print('Um dos números digitados é inválido')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos and len(operador) > 1:
        print('Operador digitado é inválido')
        continue

    print('Realizando sua operação:')
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('Erro desconhecido')



    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    #print(sair)

    if sair is True:
        break