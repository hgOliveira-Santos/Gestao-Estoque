import mysql.connector
import bcrypt
from conexão_estoque import ConexãoEstoqueBD

class UsuáriosBD(ConexãoEstoqueBD):
    def __init__(self, host="localhost", user="root", password="", nome=None, email=None, data=None, senha=None):
        super().__init__(host, user, password)
        self.nomeUsuário = nome
        self.emailUsuário = email
        self.dataCadastro = data
        self.senhaUsuário = senha
        self.senhaCriptografada = self.criptografar_senha()
        self.criar_tabela_usuários()

    def criar_tabela_usuários(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Usuarios(
                                usuarioID INT AUTO_INCREMENT PRIMARY KEY,
                                nomeUsuario VARCHAR(255),
                                emailUsuario VARCHAR(255),
                                dataCadastro VARCHAR(255),
                                senhaUsuario VARCHAR(255))""")
            
            self.conexão.commit()

        except mysql.connector.Error as e:
            print(f"Erro ao criar tabela usuarios: {e}")

    def criptografar_senha(self):
        try:
            complemento = bcrypt.gensalt()
            nova_senha = bcrypt.hashpw(self.senhaUsuário.encode('utf-8'), complemento)
            return nova_senha

        except Exception as e:  
            print(f"Erro ao criptografar senha: {e}")

app = UsuáriosBD()