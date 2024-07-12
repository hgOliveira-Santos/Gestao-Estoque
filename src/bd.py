import mysql.connector

class gerenciadorBD():
    def __init__(self, host="localhost", user="root", password=""):
        self.host = host
        self.user = user
        self.password = password
        self.conexao = None
        self.cursor = None
        self.conectar_bd()
        
    def conectar_bd(self):
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )

        self.cursor = self.conexao.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS inventario_bd")
        print("Database 'inventario_bd' criada!")
        self.cursor.execute("USE inventario_bd")
        print("Database 'inventario_bd' em uso!")

        self.criarTabelaFornecedores()
        self.criarTabelaVendas()
        self.criarTabelaProdutos()
        print("Tabelas criadas!")

        self.conexao.commit()

    def criarTabelaFornecedores(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Fornecedores(
                            fornecedorID INT AUTO_INCREMENT PRIMARY KEY,
                            nomeFornecedor VARCHAR(255) NOT NULL,
                            cidade VARCHAR(255) NOT NULL,
                            regiao VARCHAR(255) NOT NULL,
                            contato VARCHAR(255) NOT NULL)""")
        
        self.conexao.commit()

    def criarTabelaVendas(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Vendas(
                            vendaID INT AUTO_INCREMENT PRIMARY KEY,
                            produtoVendido VARCHAR(255) NOT NULL,
                            dataVenda DATE NOT NULL,
                            valorUnitario DECIMAL(10, 2) NOT NULL,
                            quantidadeVendida INT NOT NULL,
                            valorTotal DECIMAL(10, 2) NOT NULL)""")
        
        self.conexao.commit()

    def criarTabelaProdutos(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Produtos(
                            produtoID INT AUTO_INCREMENT PRIMARY KEY,
                            nomeProduto VARCHAR(255) NOT NULL,
                            descricao TEXT,
                            categoria VARCHAR(255) NOT NULL, 
                            valorUnitario DECIMAL(10, 2) NOT NULL,
                            qtdEstoque INT NOT NULL,
                            fornecedorID INT,
                            nomeFornecedor VARCHAR(255),
                            FOREIGN KEY (fornecedorID) REFERENCES Fornecedores(fornecedorID))""")
        
        self.conexao.commit()

    def inserirProduto(self):
        pass

    def inserirFornecedor(self):
        pass

    def atualizarVendas(self):
        pass
        
app = gerenciadorBD()