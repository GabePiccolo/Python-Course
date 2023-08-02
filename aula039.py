"""
Iterando Strings com While

"""

name = 'Gabriel'
name_len = len(name)

# print(name)
# print(name_len)

indice = 0
new_name = ''
while indice < name_len:
    new_name += f'{name[indice]}*'
    indice += 1
print(new_name)
