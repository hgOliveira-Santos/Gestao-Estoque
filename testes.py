import matplotlib.pyplot as plt

def criar_grafico():
    # Dados para o gráfico
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    
    # Criação do gráfico
    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title("Gráfico Exemplo")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    
    # Salva o gráfico como uma imagem
    plt.savefig("grafico.png")
    plt.close()


import flet as ft

def main(page: ft.Page):
    # Crie o gráfico e salve a imagem
    criar_grafico()
    
    # Adiciona o gráfico como uma imagem à aplicação Flet
    imagem_grafico = ft.Image(src="grafico.png", width=600, height=400)
    
    # Adiciona o widget de imagem à página
    page.add(imagem_grafico)

# Executa a aplicação Flet
ft.app(target=main)
