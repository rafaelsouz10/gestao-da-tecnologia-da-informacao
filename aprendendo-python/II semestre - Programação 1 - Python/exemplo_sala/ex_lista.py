list_a = [1, 2, 3, 4, 5, 6]
#lista_b = list_a[:]        #duplica a list_a

list_a.append(10) #adiciona o elemento no final
list_a.insert(1,99) #insere 99 na posição 1

print(list_a)

#del list_a[1] remove 
print(list_a.pop(5)) #remove o índice 5 

print(list_a)
#print("==", list_a == lista_b)  #compara a lista
#print("is", list_a is lista_b)  #compara a memória onde tá armazenado

paises = [['Brasil', 'Canadá'], 'Argentina', 'Chile']   #lista dentro de lista
print(paises[0])

#métodos para lista index(), sort(), reverse(), count(), copy(), entre outros
#métodos para python max(), min(), sum(), sorted()'ordem alfabética temporária' 

media = sum(list_a)/len(list_a)
print(media)