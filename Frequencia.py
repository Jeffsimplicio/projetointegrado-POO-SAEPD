from datetime import date

class Frequencia:
    def __init__(self, id_frequencia: int, id_aluno: int, data: date, presente: bool):
        self.id_frequencia = id_frequencia
        self.id_aluno = id_aluno
        self.data = data
        self.presente = presente