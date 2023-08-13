fatorial_lista = []

def fatorial(num):
    fatorial_num = 1
    for i in range(2, num+1):
        fatorial_num *= i
        fatorial_lista.append(str(i))
    return fatorial_num

num = int(input('Insira um número: '))
fatorial(num)
mult_fatorial = '*'.join(fatorial_lista)
print(f'{num}! --> {mult_fatorial} = {fatorial(num)}')
input()