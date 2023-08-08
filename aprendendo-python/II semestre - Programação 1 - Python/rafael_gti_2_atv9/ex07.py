"""7- Faça um programa que receba uma lista de frases. Ao final, deverá
mostrar uma nova lista de forma inversa. Veja um exemplo:
frase = ["Hoje é dia de prova de Prog1", "A prova está muito fácil", "Vou
tirar uma boa nota"]
invertidade = ["Aton aob amu rarit uov", "Licáf otium átse avorp a","1gorP ed avorp ed aid é ejoh"]"""
frase=[]
while True:
    frase.append(input('Insira uma frase: '))
    para= input("Digite '0' para parar a entrada de frases: ")
    if para=='0':
        break
print(frase)
invertidade=[]
for i in frase[::-1]:
    invertidade.append(i[::-1])
print(invertidade)