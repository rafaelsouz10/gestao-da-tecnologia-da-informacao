'''2- Faça um dicionário com 5 pessoas, tendo o nome como chave e a cor da camisa como valor. 
Logo após, imprima todas as informações do dicionário.'''

vestiario = {}
for i in range(5):
    nome = input(f'Insira o nome da {i+1}ª pessoa: ')
    cor_camisa = input(f'Insira a cor da camisa de {nome}: ')            
    vestiario[nome] = cor_camisa
print('\n\n')
for nome, cor_camisa in vestiario.items():
    print(f'{nome} e camisa da cor: {cor_camisa}')
    
