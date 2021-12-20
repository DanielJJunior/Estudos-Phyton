velocidade = float(input('digite a velocidade '))
tempo = float(input('digite o tempo '))


distancia = velocidade * tempo
litros_utilizados = distancia/12
litros_arredondados = round(litros_utilizados, 2)

print(f'com a distancia: {distancia} metros, serão necessarios {litros_arredondados} litros de combustivel')