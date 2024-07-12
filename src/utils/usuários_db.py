import mysql.connector
import bcrypt

class usuáriosBD():
    def __init__(self, nome, email, data, senha):
        self.nomeUsuário = nome
        self.emailUsuário = email
        self.dataCadastro = data
        self.senhaUsuário = senha

        self.conexão = None
        self.cursor = None
        self.conectarBD()
        self.criptografarSenha()

    def conectar_usuarios(self):
        try:     
            self.conexão = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = ""
            )

            self.cursor = self.conexão.cursor()
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS gest_usuarios")
            print("Database gest_usuarios criada!")
            self.cursor.execute("USE gest_usuarios")
            print("Database gest_usuarios em uso!")

            
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")

    def criar_tabela_usuários(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Usuarios(
                                usuarioID INT AUTO_INCREMENT PRIMARY KEY,
                                nomeUsuario VARCHAR(255),
                                emailUsuario VARCHAR(255),
                                dataCadastro VARCHAR(255),
                                senhaUsuario VARCHAR(255))""")

        
        except mysql.connector.Error as e:
            print(f"Erro ao criar tabela usuarios: {e}")


    def criptografar_senha(self):
        try:
            complemento = bcrypt.gensalt()
            nova_senha = bcrypt.hashpw(self.senhaUsuário.encode('utf-8'), complemento)
            self.senhaUsuário = nova_senha
            print(self.senhaUsuário)

        except Exception as e:
            print(f"Erro ao criptografar senha: {e}")

app = usuáriosBD("Hugo", "hgo2s@gmail.com", "2024/07/12", "hgzx7")