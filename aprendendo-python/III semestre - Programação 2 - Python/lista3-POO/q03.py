"""3. Classe Aluno: Implemente uma classe Aluno, que deve ter os seguintes 
atributos: nome, curso, tempo_sem_dormir (em horas). Essa classe deverá ter os seguintes
métodos:
    estudar(que recebe como parâmetro a qtd_de_horas de estudo e acrescenta tempo_sem_dormir);
    dormir(que recebe como parâmetro a qtd_de_horas de sono e reduz tempo_sem_dormir);
Crie um código de teste da classe, criando um objeto da classe aluno e usando os métodos estudar e dormir. 
Ao final imprima quanto tempo o aluno está sem dormir."""

class Aluno:
    def __init__(self, nome, curso, tempo_sem_dormir):
        self.nome = nome
        self.curso = curso
        self.tempo_sem_dormir = tempo_sem_dormir
    
    def estudar(self, qtd_hr_estudo):
        self.tempo_sem_dormir += qtd_hr_estudo
        return print(f'Quantidade de horas sem dormir mais hora de estudo {self.tempo_sem_dormir}')
    
    def dormir(self, qtd_hr_sono):        
        self.tempo_sem_dormir -= qtd_hr_sono
        return print(f'Quantidade de horas sem dormir menos horas de sono {self.tempo_sem_dormir}')

aluno1 = Aluno('Rafael', 'GTI', 18)

qtd_hr_estudo = int(input('Insira a quantidade de horas de estudo: '))
aluno1.estudar(qtd_hr_estudo)

qtd_hr_sono = int(input('Insira a quantidade de horas de sono: '))
aluno1.dormir(qtd_hr_sono)