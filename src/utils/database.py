import mysql.connector

class GestaoEstoque:
    def __init__(self, host="localhost", user="root", password=""):
        self.host = host
        self.user = user
        self.password = password
        self.conexao = None
        self.cursor = None
        self.conectarDatabase()
        
    def conectarDatabase(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )

            self.cursor = self.conexao.cursor()

            # Criar o esquema principal
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS gestao_estoque")
            self.cursor.execute("USE gestao_estoque")
            print("Database 'gestao_estoque' em uso!")

            self.conexao.commit()

        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")