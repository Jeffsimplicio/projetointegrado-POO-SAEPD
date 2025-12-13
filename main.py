import json
import os

ARQUIVO = "sistema.json"

# ============================
# FUNÇÕES AUXILIARES
# ============================

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        dados = {
            "professores": [],
            "alunos": [],
            "responsaveis": [],
            "turmas": [],
            "notas": [],
            "frequencias": [],
            "justificativas": [],
            "mensagens": [],
            "ocorrencias": [],
            "comportamentos": []
        }
        salvar_dados(dados)
        return dados

def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# ============================
# LOGIN
# ============================

class Login:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def validacao_user(self):
        try:
            with open('dados.json', 'r', encoding='utf-8') as dados:
                lista_dados = json.load(dados)
                for usuario in lista_dados:
                    if usuario['user'] == self.user and usuario['password'] == self.password:
                        print(f"✅ Login efetuado com sucesso! Bem-vindo {self.user} ({usuario['nivel']})")
                        return usuario['nivel']
                print("❌ Usuário ou senha inválidos")
                return None
        except FileNotFoundError:
            print("Arquivo dados.json não encontrado!")
            return None

# ============================
# CRUD GENÉRICO
# ============================

def cadastrar(entidade, campos):
    dados = carregar_dados()
    lista = dados[entidade]
    novo_id = len(lista) + 1
    registro = {"id": novo_id}
    for campo in campos:
        registro[campo] = input(f"{campo}: ")
    lista.append(registro)
    dados[entidade] = lista
    salvar_dados(dados)
    print(f"✅ {entidade.capitalize()} cadastrado com sucesso!")

def listar(entidade):
    dados = carregar_dados()
    lista = dados[entidade]
    if lista:
        print(f"\n📘 Lista de {entidade.capitalize()}:")
        for item in lista:
            print(item)
    else:
        print(f"❌ Nenhum {entidade} cadastrado.")

def editar(entidade):
    dados = carregar_dados()
    listar(entidade)
    id_editar = input(f"Digite o ID do {entidade} que deseja editar: ")
    for item in dados[entidade]:
        if str(item["id"]) == id_editar:
            for campo in item.keys():
                if campo != "id":
                    novo_valor = input(f"Novo {campo} ({item[campo]}): ")
                    if novo_valor:
                        item[campo] = novo_valor
            salvar_dados(dados)
            print(f"✅ {entidade.capitalize()} atualizado com sucesso!")
            return
    print(f"❌ {entidade.capitalize()} não encontrado.")

def excluir(entidade):
    dados = carregar_dados()
    listar(entidade)
    id_excluir = input(f"Digite o ID do {entidade} que deseja excluir: ")
    dados[entidade] = [item for item in dados[entidade] if str(item["id"]) != id_excluir]
    salvar_dados(dados)
    print(f"✅ {entidade.capitalize()} excluído com sucesso!")

# ============================
# MENUS
# ============================

def menu_admin():
    while True:
        print("\n--- MENU ADMIN ---")
        print("1 - Professores")
        print("2 - Alunos")
        print("3 - Responsáveis")
        print("4 - Turmas")
        print("5 - Notas")
        print("6 - Frequências")
        print("7 - Justificativas")
        print("8 - Mensagens")
        print("9 - Ocorrências")
        print("10 - Comportamentos")
        print("0 - Sair")
        opcao = input("Escolha: ")
        entidades = {
            "1": "professores",
            "2": "alunos",
            "3": "responsaveis",
            "4": "turmas",
            "5": "notas",
            "6": "frequencias",
            "7": "justificativas",
            "8": "mensagens",
            "9": "ocorrencias",
            "10": "comportamentos"
        }
        if opcao in entidades:
            submenu(entidades[opcao])
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida")

def submenu(entidade):
    while True:
        print(f"\n--- {entidade.capitalize()} ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Excluir")
        print("0 - Voltar")
        opcao = input("Escolha: ")
        if opcao == "1":
            campos = definir_campos(entidade)
            cadastrar(entidade, campos)
        elif opcao == "2":
            listar(entidade)
        elif opcao == "3":
            editar(entidade)
        elif opcao == "4":
            excluir(entidade)
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida")

def definir_campos(entidade):
    campos_por_entidade = {
        "professores": ["nome", "email", "disciplina", "login", "senha"],
        "alunos": ["nome", "data_nascimento", "id_turma", "id_responsavel"],
        "responsaveis": ["nome", "email", "telefone", "login", "senha"],
        "turmas": ["nome", "serie", "turno", "id_professor"],
        "notas": ["id_aluno", "id_professor", "disciplina", "valor", "data"],
        "frequencias": ["id_aluno", "data", "presente"],
        "justificativas": ["id_responsavel", "id_aluno", "tipo", "descricao", "data", "anexo"],
        "mensagens": ["id_remetente", "id_destinatario", "tipo_remetente", "assunto", "conteudo", "data_envio", "lida"],
        "ocorrencias": ["id_aluno", "id_professor", "tipo", "descricao", "data"],
        "comportamentos": ["id_aluno", "id_professor", "avaliacao", "observacoes", "data"]
    }
    return campos_por_entidade.get(entidade, [])

# ============================
# PROGRAMA PRINCIPAL
# ============================

def main():
    print("-"*10, "Bem-vindo ao SAEPD", "-"*10)
    user = input("Usuário: ")
    password = input("Senha: ")
    login = Login(user, password)
    nivel = login.validacao_user()
    if nivel == "admin":
        menu_admin()
    elif nivel == "professor":
        submenu("notas")
    elif nivel == "responsavel":
        submenu("justificativas")

if __name__ == "__main__":
    main()