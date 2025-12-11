import json

class Login:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def validacão_user(self):
        
        with open('dados.json', 'r', encoding='utf-8') as dados:
            lista_dados= json.load(dados)
            for i in range(len(lista_dados)):
                if lista_dados[i]['user'] == self.user:
                    if lista_dados[i]['password'] == self.password:
                        print("login feituado") 
                        return True
            
            print("usuario nao encontrado")

                    


print("-"*10,"bem vindo ao SAEPD","-"*10)


user = str(input("usuario: "))
password = str(input("senha: "))
login = Login(user, password)
login.validacão_user()
 
        
    