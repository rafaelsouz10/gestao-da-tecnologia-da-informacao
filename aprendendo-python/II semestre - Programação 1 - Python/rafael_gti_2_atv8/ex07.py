"""7- Sabendo que A = {0, 1, 2, 3, 4, 5, 6}, B = {6, 7, 8, 9} e C = {2, 4, 6, 8, 10}:
Apresente a:
    1. união dos 3 conjuntos:
    2. interseção dos 3 conjuntos:
    3. interseção entre A e C:
    4. interseção entre B e C:
    5. diferença entre B e A:
    6. diferença entre C e A:
    7. diferença simétrica entre B e C:"""
A = {0, 1, 2, 3, 4, 5, 6}; B = {6, 7, 8, 9}; C = {2, 4, 6, 8, 10}

print(f"""
    1. União dos 3 conjuntos: {A.union(B,C)}
    2. interseção dos 3 conjuntos: {A.intersection(B,C)}
    3. interseção entre A e C: {A.intersection(C)}
    4. interseção entre B e C: {B.intersection(C)}
    5. diferença entre B e A: {B.difference(A)}
    6. diferença entre C e A: {C.difference(A)}
    7. diferença simétrica entre B e C: {B.symmetric_difference(C)}
""")