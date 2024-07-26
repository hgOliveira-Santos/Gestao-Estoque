import flet as ft

def main(page):
    page.title = "Gestão de Inventário"
    page.window_min_width = 400
    page.window_min_height = 600

    page_width = page.width

    # Função para manipular o clique do botão
    def on_button_click(index):
        print(f"Destino selecionado: {index}")

    # Itens de navegação
    nav_items = [
        {"icon": ft.icons.HOME, "label": "Início"},
        {"icon": ft.icons.INVENTORY, "label": "Estoque"},
        {"icon": ft.icons.SELL, "label": "Vendas"},
        {"icon": ft.icons.FACTORY, "label": "Fornecedores"},
        {"icon": ft.icons.SHOW_CHART, "label": "Relatório"}
    ]

    # Criar uma lista de botões com ícones e textos
    nav_buttons = [
        ft.IconButton(
            content=ft.Row(
                controls=[
                    ft.Icon(item["icon"], size=24),  # Ajuste o tamanho do ícone conforme necessário
                    ft.Text(value=item["label"], size=20)  # Ajuste o tamanho da fonte aqui
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            on_click=lambda e, idx=i: on_button_click(idx),
            style=ft.ButtonStyle(
                padding=ft.Padding(top=10, right=10, bottom=10, left=25),
                color=ft.colors.WHITE70
            )
        )
        for i, item in enumerate(nav_items)
    ]

    page.add(
        ft.Row(
            controls=[
                ft.Container(
                    bgcolor=ft.colors.DEEP_PURPLE_800,
                    margin=ft.Margin(top=-10, bottom=-10, left=-10, right=-10),
                    width=page.width*0.25,
                    expand=False,
                    content=ft.Container(
                        bgcolor=ft.colors.DEEP_PURPLE_800,
                        margin=ft.Margin(top=80, bottom=-10, left=20, right=20),
                        content=ft.Column(
                            controls=nav_buttons,
                            spacing=15,
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START
                        )
                    )
                ),
                ft.Container(
                    bgcolor=ft.colors.BLACK38,
                    margin=ft.Margin(top=-10, bottom=-10, left=0, right=-10),
                    expand=True
                )
            ],
            expand=True
        )
    )

ft.app(target=main)
