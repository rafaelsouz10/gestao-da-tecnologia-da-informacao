codigos = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lista_secreta = [2, 15, 13, 0, 4, 9, 1]
traduzir = []
for i in lista_secreta:
    traduzir.append(codigos[i])
print(f"{lista_secreta = } --> {''.join(traduzir)}")

codificar = []
nome = 'rafael'
for letra in nome:
    codificar.append(codigos.index(letra))
print(nome, '-->', codificar)