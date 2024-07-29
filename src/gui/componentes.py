import flet as ft

def on_button_click(index):
    print(f"Destino selecionado: {index}")

nav_items = [
        {"icon": ft.icons.HOME, "label": "Início"},
        {"icon": ft.icons.INVENTORY, "label": "Estoque"},
        {"icon": ft.icons.SELL, "label": "Vendas"},
        {"icon": ft.icons.FACTORY, "label": "Fornecedores"},
        {"icon": ft.icons.SHOW_CHART, "label": "Relatório"}
    ]

botões_barra_lateral = [
    ft.IconButton(
        content=ft.Row(
            controls=[
                ft.Icon(item["icon"], size=24),
                ft.Text(value=item["label"], size=20)  
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


barra_lateral = ft.Container(
                        bgcolor=ft.colors.DEEP_PURPLE_800,
                        margin=ft.Margin(top=-10, bottom=-10, left=-10, right=-10),
                        width=250,
                        expand=False,
                        content=ft.Container(
                            bgcolor=ft.colors.DEEP_PURPLE_800,
                            margin=ft.Margin(top=90, bottom=-10, left=20, right=20),
                            content=ft.Column(
                                controls=botões_barra_lateral,
                                spacing=15,
                                alignment=ft.MainAxisAlignment.START,
                                horizontal_alignment=ft.CrossAxisAlignment.START
                            )
                        )
                    )

cabeçalho = ft.Container(
                bgcolor=ft.colors.BLACK38,
                margin=ft.Margin(top=-10, bottom=0, left=0, right=-10),
                height=60,
                content=ft.Row(
                    controls=[
                        ft.Text(value="Tech Essentials", size=20, font_family="Inter", color=ft.colors.WHITE)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    )
                )
    
início = ft.Container(
            bgcolor=ft.colors.WHITE,
            expand=True,
            margin=ft.Margin(top=-10, bottom=-10, left=0, right=-10),
        )   