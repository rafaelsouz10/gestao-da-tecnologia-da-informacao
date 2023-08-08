faltas = [[ 'Brasil', 'Italia', [10, 9] ], 
         [ 'Brasil', 'Espanha', [5, 6] ], 
         [ 'Italia', 'Espanha', [7, 8] ]]
faltas_bra = faltas[0][2][0]+faltas[1][2][0]
faltas_ita = faltas[0][2][1]+faltas[2][2][0]
faltas_esp = faltas[1][2][1]+faltas[2][2][1]

times = [faltas[0][0], faltas[0][1], faltas[1][1]]  #Brasil, Italia, Espanha na respectiva ordem
total_faltas = [faltas_bra, faltas_ita, faltas_esp]
indice_max_faltas = total_faltas.index(max(total_faltas))
indice_min_faltas = total_faltas.index(min(total_faltas))

print(f'Total de faltas do campeonato: {sum(total_faltas)}')
print(f'O time que fez mais faltas: {times[indice_max_faltas]}')
print(f'O time que fez mais faltas: {times[indice_min_faltas]}')