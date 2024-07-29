import mysql.connector

class ConexãoEstoqueBD():
    def __init__(self, host="localhost", user="root", password=""):
            self.host = host
            self.user = user
            self.password = password
            self.conexão = None
            self.cursor = None
            self.conectar_estoque()

    def conectar_estoque(self):
        try:
            self.conexão = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )

            self.cursor = self.conexão.cursor()
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS gestao_estoque")
            print("Database 'gestao_estoque' criada!")
            self.cursor.execute("USE gestao_estoque")
            print("Database 'gestao_estoque' em uso!")

            self.conexão.commit()

        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")