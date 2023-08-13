'''2. Classe Conta Corrente: Crie uma classe para implementar uma conta
corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do
correntista e saldo. Os métodos são os seguintes: alterar_nome, deposito e
saque;
No construtor, saldo é opcional, com valor default (padrão) zero e os demais
atributos são obrigatórios.'''

from os import system

class Conta_corrente:
    def __init__(self, num_conta, nome_correntista, saldo=0):
        self.num_conta = num_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    
    def alterar_nome(self):
        self.nome_correntista = input('Insira o novo nome do correntista: ')
        print(f'\nNovo nome {self.nome_correntista} cadastrado sucesso.')
    
    def depositar(self):
        input('\nClique em algo para continuar...')
        system('cls')

        while True:
            deposito = float(input(f'{self.nome_correntista}, insira o valor do depósito: '))
            if deposito > 0:
                self.saldo += deposito
                break
            else:
                print('\nDepósito inválido.')
        print(f'\nDeposito de R$ {deposito:.2f} efetuado com sucesso.\nSaldo: R$ {self.saldo:.2f}')

    def saque(self):
        input('\nClique em algo para continuar...')
        system('cls')
        while True:
            saque = float(input('Insira o valor do saque: '))
            if 0 < saque < self.saldo:
                self.saldo -= saque
                break
            else:
                print('\nSaque inválido.')
        print(f'\nSaque de R$ {saque:.2f} efetuado com sucesso.\nSaldo: R$ {self.saldo:.2f}')

conta1 = Conta_corrente(12345, 'Rafael')
print(f'Conta 12345, Correntista Rafael.\n')

conta1.alterar_nome()
conta1.depositar()
conta1.saque()