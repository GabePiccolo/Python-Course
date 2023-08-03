frase = 'O python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido von Rossum.'

i = 0

qtd_mais_vezes = 0
letra_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_mais_vezes_atual = frase.count(letra_atual)

    if qtd_mais_vezes < qtd_mais_vezes_atual:
        qtd_mais_vezes = qtd_mais_vezes_atual
        letra_mais_vezes = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi ' f'"{letra_mais_vezes}" ' f'({qtd_mais_vezes}x)')
