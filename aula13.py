nome = 'Gabe Piccolo'
altura = 1.75
peso = 82
imc = peso / (altura ** 2)

# Gabe Piccolo tem 1.75 de altura,
# pesa 82 quilos e seu IMC é
# 26.X

#Introdução a F-Strings:
fstring1= f'{nome} tem {altura:.2f} de altura,\npesa {peso} quilos e seu IMC é\n{imc:.2f}'

print(fstring1)