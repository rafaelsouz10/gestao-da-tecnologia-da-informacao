num = int(input('Insira um número e saiba o seu fatorial: '))

fatorial= 1

print(f'\n{num}! --> {fatorial}', end='')
for i in range(2, num+1):
    fatorial *= i
    print(f' * {i}', end='')

print(f' == {fatorial}\n')