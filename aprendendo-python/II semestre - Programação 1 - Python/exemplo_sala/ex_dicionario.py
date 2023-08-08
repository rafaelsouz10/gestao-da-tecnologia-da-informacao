agenda = {"Maria": [999112233, 98822324],
          "Joao": 98923212,
          "Joaquim": 99933173,
          'Silvana': 'Sem Telefone'}
print('\n\n')

# chave='Rafael' e valor=999113174
agenda['Rafael'] = [999113174]
print(agenda)
print(agenda['Maria'][1])
print('\n\n')

# já assume como uma string
agenda2 = dict(caio=12345)
print(agenda2)
print('\n\n')

# remover chave do dicionario
agenda.pop('Joao')
del agenda['Joaquim']
print(agenda)
print('\n\n')

# verificar se existe chave na agenda
print(agenda.get('rafael', 'Não existe'))
print('\n\n')

# pega somente as chaves
for chave in agenda:
    print(chave)
print('\n\n')

# pega o valor das chaves
for chave in agenda:
    print(chave, agenda[chave])

for valor in agenda.values():
    print(valor)
print('\n\n')

# puxa os dois valores ao mesmo tempo
for chave, valor in agenda.items():
    print(chave, valor)
print('\n\n')

#dicionario com dicionario dentro
funcionarios = {
    'valeria': {'cargo': 'coordenadora', 'salario': 5000},
    'Donato': {'cargo': 'Estagiario', 'salario': 500},
}
print(funcionarios['valeria']['salario'])
nome = input('Insira o nome do funcionario: ')
print(f"Salario de {nome}: R$ {funcionarios[nome]['salario']}")
print('\n\n')

print(funcionarios.get(nome, 'Não encontrado')) #caso o usuario digitar um valor inexistente

if nome in funcionarios:
    print(nome)
    print("Cargo: ", funcionarios[nome]['cargo'])
    print('salario: ', funcionarios[nome]['salario'])