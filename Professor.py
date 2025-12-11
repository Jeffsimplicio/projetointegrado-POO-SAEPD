class Professor:
    def __init__(self, id_professor: int, nome: str, email: str, disciplina: str, login: str, senha: str):
        self.id_professor = id_professor
        self.nome = nome
        self.email = email
        self.disciplina = disciplina
        self.login = login
        self.senha = senha
        # Criando um objeto da classe Professor
prof1 = Professor(
    id_professor=1,
    nome="Maria Silva",
    email="maria.silva@escola.com",
    disciplina="Matemática",
    login="msilva",
    senha="12345"
)

# Acessando atributos
print(prof1.nome)        # Maria Silva
print(prof1.disciplina)  # Matemática
