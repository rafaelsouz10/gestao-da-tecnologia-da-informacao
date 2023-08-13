"""Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
▪
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
▪
Utilize métodos para alterar o canal e o volume da TV.
▪
Certifique-se que o número do canal e o nível do volume permaneçam dentro de faixas válidas.
o
Obs.: As faixas válidas ficam à critério do(a) aluno(a)."""

class TV:
    def __init__(self):
        self.canal = 9
        self.volume = 60
    
    def altera_volume(self, novo_volume):
        if 0<=novo_volume<=100:
            self.volume = novo_volume
        else:
            print("Faixa de volume inválida")
        print('Volume Atual: ', self.volume)
    
    def altera_canal(self, novo_canal):
        if 0<=novo_canal<=100:
            self.canal = novo_canal
        else:
            print("Canal inválido")
        print('Canal Atual: ', self.canal)

tv = TV()

tv.altera_volume(int(input('Insira um Volume: ')))
tv.altera_canal(int(input('Insira um Canal: ')))
