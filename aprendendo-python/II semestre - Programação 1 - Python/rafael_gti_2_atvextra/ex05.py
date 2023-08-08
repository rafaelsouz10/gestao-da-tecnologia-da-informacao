"""5. Faça um programa que escreva um número digitado pelo usuário por extenso 
aceitando números de até 3 dígitos, use listas de strings para guardar cada tradução
 (ex.: unidades = [“zero”, “um”, “dois”, ..., “nove”]).
Exemplo:
    Usuário digita: 395
    Resultado: trezentos e noventa e cinco."""
unidades = ['zero', 'um', 'dois', 'três', 'quatro' ,'cinco', 'seis', 'sete', 'oito', 'nove']
dezenas = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
centenas = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
resultado = []

while True:
    num = list((input('Insira um número até 3 digitos: ')))
    if len(num) <= 3:
        break
if len(num) == 3:
    resultado.insert(0, centenas[int(num[0])-1])
    resultado.insert(1, dezenas[int(num[1])-1])
    resultado.insert(2, unidades[int(num[2])])
elif len(num) == 2:
    resultado.insert(0, dezenas[int(num[0])-1])
    resultado.insert(1, unidades[int(num[1])])
elif len(num) == 1:
    resultado.insert(0, unidades[int(num[0])])
print(' e '.join(resultado))