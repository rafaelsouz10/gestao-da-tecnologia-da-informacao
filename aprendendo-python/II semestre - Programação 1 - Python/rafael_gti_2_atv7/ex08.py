"""8- Faça um programa que crie uma lista (com valores informados pelo usuário) e mostre a
lista com o dobro dos valores lidos (2 * item)."""
lista= []; dobro= []
for i in range(5):
    valor= float(input('Insira um numero: '))
    lista.append(valor)
    dobro.append(valor*2)
print(lista)
print(dobro)