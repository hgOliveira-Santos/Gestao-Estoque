import mysql.connector

class GestãoInventárioBD():
    def __init__(self, host="localhost", user="root", password=""):
            self.host = host
            self.user = user
            self.password = password
            self.conexão = None
            self.cursor = None
            self.conectar_inventário()

    def conectar_inventário(self):
        try:
            self.conexão = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )

            self.cursor = self.conexão.cursor()
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS gestao_inventario")
            print("Database 'gestao_inventario' criada!")
            self.cursor.execute("USE gestao_inventario")
            print("Database 'gestao_inventario' em uso!")

            self.conexão.commit()

        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")