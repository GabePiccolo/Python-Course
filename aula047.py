"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

word = 'ferrari'
secret = '*'
correct_letters = ''
try_num = 0

while True:

    try_num += 1
    type = input('Type a single letter: ')

    if len(type) > 1:
        print('Type just one letter!')
        continue

    if type in word:
        correct_letters += type

    final_word = ''
    for i in word:
        if i in correct_letters:
            final_word += i
        else: 
            final_word += secret
    print(final_word)

    if final_word == word:
        os.system('cls')
        print('YOU WON!')
        print('Number of attempts:', try_num)
        break
        
     