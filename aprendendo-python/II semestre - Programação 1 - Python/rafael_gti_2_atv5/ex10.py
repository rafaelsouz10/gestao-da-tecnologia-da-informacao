fraseA= input('Insira uma Frase: ')
fraseB= input('Insira outra Frase: ')

fraseC = fraseB+fraseA
for i in fraseC:
    if i in 'A':
        fraseC= fraseC.replace('A', '*')
print(fraseC)