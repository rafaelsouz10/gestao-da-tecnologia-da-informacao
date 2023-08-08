"""3. Faça um programa que, dados dois inteiros x e y, 
crie uma lista com todos os valores entre x e y (inclusive), 
funcionando tanto para x <= y como para x > y.
Exemplos:
    x = 2, y = 6, resultado = [2, 3, 4, 5, 6]
    x = 10, y = 7, resultado = [10, 9, 8, 7]"""
num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))
lista = []
if num1 > num2:
    for i in range(num2, num1+1):
        lista.append(i)
else:
    for i in range(num2, num1-1, -1):
        lista.append(i)
print(lista)
