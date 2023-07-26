"""
CONSTANTE =  "Variáveis" que não vão mudar
Muitas condições no mesmo if é considerado ruim
     <- Contagem de complexidade (ruim)
"""
velocidade = 60 # velocidade atual do carro
km_do_carro = 100 # km da rodovia onde o carro se encontra

RADAR_1 = 60 # velocidade máxima do Radar 1
KM_1 = 100 # km da rodovia onde o radar se encontra
RADAR_RANGE = 1 # a distância onde o radar captura

vel_acima = velocidade > RADAR_1
km_range_maior = KM_1 + RADAR_RANGE
km_range_menor = KM_1 - RADAR_RANGE
carro_passou_radar1 = km_do_carro >= km_range_menor \
      and km_do_carro <= km_range_maior

carro_multado = carro_passou_radar1 and vel_acima

if carro_multado:
    print('O carro passou na velocidade acima da permitida e foi multado!')
elif carro_passou_radar1 and not vel_acima:
    print('O carro passou na velocidade permitida')    