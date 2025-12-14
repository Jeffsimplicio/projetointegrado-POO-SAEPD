from abc import ABC, abstractmethod

class Usuario(ABC):
    """
    Classe Abstrata Base para todos os perfis de usuário do SAEPD.
    Define o contrato de métodos obrigatórios (Polimorfismo) para:
    Professor, Responsavel e Administrador.
    """
    
    def __init__(self, id_usuario: str, nome: str, email: str, senha: str):
        # Encapsulamento de dados
        self._id = id_usuario
        self._nome = nome
        self._email = email
        self._senha = senha # Idealmente, armazenaríamos o hash da senha
    
    # Métodos Getters para acesso controlado aos atributos
    @property
    def id(self):
        return self._id
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def email(self):
        return self._email

    # Método abstrato obrigatório (Polimorfismo)
    @abstractmethod
    def apresentar_painel(self):
        """
        Método obrigatório que cada classe de usuário deve implementar.
        Ele define a interface específica do perfil (painel do professor, do responsável, etc).
        """
        pass
        
    # Método não abstrato que pode ser herdado ou sobrescrito
    def realizar_login(self, email_informado: str, senha_informada: str) -> bool:
        """Verifica as credenciais de login."""
        return self._email == email_informado and self._senha == senha_informada
