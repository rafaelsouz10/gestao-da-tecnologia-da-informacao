######################################################### QUESTÃO 01
print('q01')
def soma(x,y,z):
    return x+y+z
print('Soma = ',soma(2,3,4),"\n")

######################################################### QUESTÃO 02
print('q02')
def menor(x,y):
    return min(x,y)
print("menor: ", menor(5,2))

######################################################### QUESTÃO 03
print('\nq03')
def func(num):
    inteiro = int(num)  #num*num//num #num//1
    print(f"{int(inteiro) = } ")
    fracao = num - inteiro
    print(f"{fracao = }")
func(100.25)

######################################################### QUESTÃO 04
print('\nq04')
lista = []
while True:
    num = int(input('Insira um número: '))
    para = input('Por outro número: [S]-Sim [Qualquer outro valor]-Não:  ').upper()
    lista.append(num)
    if para[0] == 'N':
        break 
def numeros(lista):
    maior = max(lista)
    qtd_maior = lista.count(maior)
    print(f"\n{lista = }\n{maior = }\n {qtd_maior = }")
numeros(lista)

######################################################### QUESTÃO 05
print('\nq05')
def opc_notas(notas, letra):
    if letra == 'A':
        aritmetica = sum(notas)/len(notas)
        print(f'Média Aritmética: {aritmetica}')
    elif letra == 'P':
        ponderada = (notas[0]*5 + notas[1]*3 + notas[2]*2) / (5+3+2)
        print(f'Média Ponderada: {ponderada}')
    elif letra == 'H':
        harmonica = 3 / ((1/notas[0]) + (1/notas[1]) + (1/notas[2]))
        print(f'Média Harmônica: {harmonica}')
    else:
        print('Caracter Inválido.')
notas = []
for i in range(3):
    notas.append(float(input(f'Insira sua {i+1}ª nota: ')))
letra = input('''\n[A]-Média Aritmética\n[P]-Média Ponderada\n[H]-Média Harmônica
Digite o caracter respectivo a média que deseja: ''').upper()
opc_notas(notas, letra)
input()

######################################################### QUESTÃO 06
print('\nq06')
def tip_num(num):
    if num > 0:
        print('Número positivo.')
    elif num == 0:
        print('Número zero neuto.')
    else:
        print('Número negativo.')
    if ((num//1)-num)==0:
        print('Número inteiro.')
        
        if num%2==0:
            print('Número par.')
        else:
            print('Número ímpar.')
    else:
        print('Número decimal.')

tip_num(float(input('Insira um número: ')))
input()

######################################################### QUESTÃO 07
print('\nq07')
def inverso_num(num):
    str_num = str(num)
    return int(str_num[::-1])
num = int(input('Insira um número: '))
inverso_num(num)
print(num,' -> ',inverso_num(num))
input()

######################################################### QUESTÃO 08
print('\nq08')
fatorial_lista = []

def fatorial(num):
    fatorial_num = 1
    for i in range(2, num+1):
        fatorial_num *= i
        fatorial_lista.append(str(i))
    return fatorial_num

num = int(input('Insira um número: '))
fatorial(num)
mult_fatorial = '*'.join(fatorial_lista)
print(f'{num}! --> {mult_fatorial} = {fatorial(num)}')
input()

######################################################### QUESTÃO 09
print('\nq09')
def peso_ideal(altura, sexo):
    if sexo == 'M':
        ideal_peso = 72 * altura - 60
    elif sexo == 'F':
        ideal_peso = 62 * altura - 50
    else:
        ideal_peso = 'Não foi possível verificar o seu peso ideal. Verifique os parâmetros inseridos.'
    return ideal_peso
sexo = input('\n[M]-Masculino\n[F]-Feminino\nInsira o caracter do seu respectivo sexo acima: ').upper()
altura = float(input('Insira a sua altura:'))
print(f'Peso ideal: ',peso_ideal(altura, sexo[0]))
input()

######################################################### QUESTÃO 10
print('\nq10')
def retangulo(altura, largura):
    if altura == 1 and largura == 0:
	print('#'*largura)
    if largura == 1 and altura == 0:
	for i in range(altura):
        	print('\n#')
    else:
    	print('#'*largura)
    	for i in range(altura-2):
        	print('#'+' '*(largura-2)+'#')
    	print('#'*largura)

retangulo(int(input('Insira a Altura: ')),int(input('Insira a Largura: ')))

retangulo(4,10)

#############
#           #
#           #
#############















