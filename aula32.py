"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número inteiro: ')

try:
    num_int = int(num)
    resto = num_int % 2

    if resto == 0:
        print('Este número é par')
    else:
        print('Este número é ímpar')
except:
    print('Este número não é inteiro ou não foi digitado um número')  

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Que horas são? ')
hora_int = int(hora)

if hora_int >= 0 and hora_int <= 11:
    print('Bom dia!')
elif hora_int >= 12 and hora_int <= 17:
    print('Boa tarde!')
elif hora_int >= 18 and hora_int <= 23:
    print('Boa noite!')
else:
    print('Valor incorreto!')        

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto!')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')    