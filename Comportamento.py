from datetime import date

class Comportamento:
    def __init__(self, id_comportamento: int, id_aluno: int, id_professor: int, 
                 avaliacao: str, observacoes: str, data: date):
        self.id_comportamento = id_comportamento
        self.id_aluno = id_aluno
        self.id_professor = id_professor
        self.avaliacao = avaliacao
        self.observacoes = observacoes
        self.data = data