import math

alunos = {}
while True:
    nome = input('Insira o nome do aluno: ').title()
    estatura = float(input('Insira a estatura do aluno: '))
    peso = float(input('Insira o peso do aluno: '))
    
    imc = peso/(pow(estatura,2))    #imc = peso/(estatura/estatura)
    alunos[nome] = imc
    exit = input('\nContinuar do cadastro? [1]-Sim [Qualquer outra tecla]-Não: ')
    if exit != '1':
        break;
print('\n------ IMC dos alunos ------\n')
for chave in sorted(alunos):
    print(f'{chave} com IMC {alunos[chave]}')