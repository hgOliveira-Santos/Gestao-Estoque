class Produtos():
    def __init__(self, nome: str, descrição: str, categoria: str, valorUnitário: int, qtdEstoque: int):
        self.nomeProduto = nome
        self.descrição = descrição
        self.categoria = categoria
        self.valorUnitário = valorUnitário
        self.qtdEstoque = qtdEstoque

    def atualizaValorUnitário(self, novoValor):
        self.valorUnitário = novoValor

    def atualizaQuantidadeEstoque(self, quantidade):
        self.qtdEstoque = quantidade
    
    