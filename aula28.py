nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print('Seu nome é:', nome)
    print('Seu nome invertido é:', nome[::-1])
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')    
    print('Seu nome tem', len(nome), 'letras')
    print('A primeira letra do seu nome é:', nome[0])
    print('A ultima letra do seu nome é:', nome[-1])
else:
    print('Desculpe, você deixou campos vazios')