'''1. Classe Filme: Construa a classe Filme, que obedeça à descrição abaixo:
A classe deve possuir dois atributos: titulo e duracao_em_minutos.
Crie um método exibir_duracao_em_horas que converta o valor em
minutos para horas e apresente a mensagem "O filme TITULO possui X
horas e Y minutos de duração".
Por exemplo, dado o filme com título Titanic que possui 194 minutos de
duração, a mensagem que deverá ser exibida para o usuário será:
"O filme Titanic possui 3 horas e 14 minutos de duração."'''
class Filme():
    def __init__(self, titulo, duracao_em_minutos):
        self.titulo = titulo
        self.duracao_em_minutos = duracao_em_minutos

    def exibir_duracao_em_horas(self):
        horas_de_filme = self.duracao_em_minutos // 60
        min_restante = self.duracao_em_minutos -  (horas_de_filme*60)
        print(f"O filme {self.titulo} tem {horas_de_filme} horas e {min_restante} minutos de duração.")

filme1 = Filme("Fash",144)
filme1.exibir_duracao_em_horas()