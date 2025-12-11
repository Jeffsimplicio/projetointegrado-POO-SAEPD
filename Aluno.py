from datetime import date

class Aluno:
    def __init__(self, id_aluno: int, nome: str, data_nascimento: date, id_turma: int, id_responsavel: int):
        self.id_aluno = id_aluno
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.id_turma = id_turma
        self.id_responsavel = id_responsavel