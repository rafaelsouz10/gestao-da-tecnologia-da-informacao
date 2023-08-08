set1 = {'a', 'b', 'c'}
set2 = {'c', 'd', 'e'}

print(f'{set1.union(set2)=}') #print(set1|set2)

print(f'{set1.intersection(set2)=}') #interseção ou -> print(set1 & set2)
print(f'{set1.symmetric_difference(set2)=}') #diferença -> set1^set2

tupla = (1,2,3)
tupla = tupla + (10,)
print(tupla)    