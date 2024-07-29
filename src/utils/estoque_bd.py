import mysql.connector
from utils.conexão_estoque import ConexãoEstoqueBD

class EstoqueBD(ConexãoEstoqueBD):
    def __init__(self, host="localhost", user="root", password=""):
        super().__init__(host, user, password)
        self.criar_tabelas()

    def criar_tabelas(self):
        self.criar_tabela_fornecedores()
        self.criar_tabela_vendas()
        self.criar_tabela_produtos()
        print("Tabelas criadas!")

        self.conexão.commit()

    def criar_tabela_fornecedores(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Fornecedores(
                                fornecedorID INT AUTO_INCREMENT PRIMARY KEY,
                                nomeFornecedor VARCHAR(255) NOT NULL,
                                contato VARCHAR(255) NOT NULL)""")
            
            self.conexão.commit()

        except mysql.connector.Error as e:
            print(f"Erro ao criar tabela Fornecedores: {e}")

    def criar_tabela_vendas(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Vendas(
                                vendaID INT AUTO_INCREMENT PRIMARY KEY,
                                produtoVendido VARCHAR(255) NOT NULL,
                                dataVenda DATE NOT NULL,
                                valorUnitario DECIMAL(10, 2) NOT NULL,
                                quantidadeVendida INT NOT NULL,
                                valorTotal DECIMAL(10, 2) NOT NULL)""")
            
            self.conexão.commit()

        except mysql.connector.Error as e:
            print(f"Erro ao criar tabela Vendas: {e}")

    def criar_tabela_produtos(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Produtos(
                                produtoID INT AUTO_INCREMENT PRIMARY KEY,
                                nomeProduto VARCHAR(255) NOT NULL,
                                tipoProduto VARCHAR(255) NOT NULL,
                                categoria VARCHAR(255) NOT NULL, 
                                valorUnitario DECIMAL(10, 2) NOT NULL,
                                qtdEstoque INT NOT NULL,
                                fornecedorID INT,
                                nomeFornecedor VARCHAR(255),
                                FOREIGN KEY (fornecedorID) REFERENCES Fornecedores(fornecedorID))""")
            
            self.conexão.commit()

        except mysql.connector.Error as e:
            print(f"Erro ao criar tabela Produtos: {e}")

    def cadastro_produto(self, produto, tipo, categoria, valor, quantidade, id_fornecedor=None, nome_fornecedor=None):
        try:
            query = """INSERT INTO Produtos (nomeProduto, tipoProduto, categoria, valorUnitario, qtdEstoque, fornecedorID, nomeFornecedor)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""

            valores = (produto, tipo, categoria, valor, quantidade, id_fornecedor, nome_fornecedor)
            self.cursor.execute(query, valores)
            self.conexão.commit()

        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar produto: {e}")

    def inserir_produto(self, nome_fornecedor, contato_fornecedor):
        try:
            query = """INSERT INTO Fornecedores (nomeFornecedor, contato)
                    VALUES (%s, %s)"""
            valores = (nome_fornecedor, contato_fornecedor)

            self.cursor.execute(query, valores)
            self.conexão.commit()

        except mysql.connector.Error as e:
            print(f"Erro ao inserir fornecedor: {e}")

    def atualiza_vendas(self):
        pass

app = InventárioBD()
app.cadastro_produto("g502", "Mouse", "Periferico", 450.00, 120)
app.cadastro_produto("Deathadder v2", "Mouse", "Periferico", 399.90, 200)