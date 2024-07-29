import flet as ft

def main(page: ft.Page):
    # Define a cor de fundo da página
    page.bgcolor = ft.colors.LIGHT_BLUE  # Você pode escolher a cor que preferir

    # Adiciona algum conteúdo para visualizar o fundo
    page.add(
        ft.Column(
            controls=[
                ft.Text("Este é um exemplo de cor de fundo", size=20, color=ft.colors.WHITE),
                ft.ElevatedButton(text="Clique aqui", color=ft.colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# Executa a aplicação Flet
ft.app(target=main)
