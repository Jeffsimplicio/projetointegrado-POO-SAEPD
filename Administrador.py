class Administrador:
    def __init__(self, id_adm: int, nome: str, email: str, login: str, senha: str):

        self.id_adm = id_adm
        self.nome = nome
        self.email = email
        self.login = login

        self.senha = senha


    # Metodo para  Cadastrar Professor
   
    def cadastrar_professor(self, id_prof, nome, email, disciplina, login, senha):
        
        novo_professor = Professor(
            id_professor=id_prof,
            nome=nome,
            email=email,
            disciplina=disciplina,
            login=login,
            senha=senha
        )
        print(f"Professor {nome} cadastrado com sucesso!")
        return novo_professor
    
    # Metodo para Cadastrar Responsavel
    
    def cadastrar_responsavel(self, id_resp, nome, email, telefone, login, senha):
        
        novo_responsavel = Responsavel(
            id_responsavel=id_resp,
            nome=nome,
            email=email,
            telefone=telefone,
            login=login,
            senha=senha
        )
        print(f"Responsável {nome} cadastrado com sucesso!")
        return novo_responsavel

   # Metodo para Cadastar Turma

   def cadastrar_turma(self, id_turma, nome, serie, turno, id_professor):
        
        nova_turma = Turma(
            id_turma=id_turma,
            nome=nome,
            serie=serie,
            turno=turno,
            id_professor=id_professor
        )
        print(f"Turma {nome} criada e vinculada ao Prof. ID {id_professor}.")
        return nova_turma

   #Metodo para Cadastrar Aluno

   def cadastrar_aluno(self, id_aluno, nome, data_nasc, id_turma, id_responsavel):
        
        novo_aluno = Aluno(
            id_aluno=id_aluno,
            nome=nome,
            data_nascimento=data_nasc,
            id_turma=id_turma,
            id_responsavel=id_responsavel
        )
        print(f"Aluno {nome} matriculado na Turma {id_turma}.")
        return novo_aluno






