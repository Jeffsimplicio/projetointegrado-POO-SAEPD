from datetime import date
from decimal import Decimal
 
#um cuidado especial com o atributo valor. Em programação financeira ou notas escolares que exigem precisão, 
#evitamos usar float (ponto flutuante) porque ele pode gerar erros de arredondamento 
#(ex: 7.1 + 0.2 pode virar 7.30000000001). Por isso, usamos o tipo Decimal.

class Nota:
    def __init__(self, id_nota: int, id_aluno: int, id_professor: int, 
                 disciplina: str, valor: Decimal, data: date):
        self.id_nota = id_nota
        self.id_aluno = id_aluno
        self.id_professor = id_professor
        self.disciplina = disciplina
        self.valor = valor
        self.data = data