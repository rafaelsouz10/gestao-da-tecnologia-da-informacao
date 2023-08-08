import os
carro = []; consumo = []
for i in range(5):
    carro.append(input(f'Insira o modelo do Veículo {i+1}: '))
    consumo.append(float(input(f'Insira quantos km/l faz o {carro[i]}: ')))
os.system('cls')
print(f"{'-'*5} Comparativo de Consumo de Combustível {'-'*5}")
for i in range(5):
    print(f"""
    Veículo {i+1}
    Nome: {carro[i]}
    Km por litro: {consumo[i]}
    """)
input('Aperte em qualquer tecla para continuar...')
os.system('cls')
print(f"{'-'*5} Relatório Final {'-'*5}")
for i in range(5):
    print(f"{i+1} - {carro[i]} - {consumo[i]} - {1000/consumo[i]:.1f} litros - R$ {(1000/consumo[i])*5.40:.2f}")
carro_consumo = carro[consumo.index(max(consumo))]
print(f'\nO menor consumo é do {carro_consumo}.')