import flet as ft
from componentes import *

def main(page: ft.Page):
    page.title = "Gestão de Estoque"
    page.window_min_width = 400
    page.window_min_height = 600
    page.bgcolor = ft.colors.BLACK87
    

    page.add(
        ft.Row(
            controls=[
                barra_lateral,
                ft.Column(
                    controls=[
                        cabeçalho,
                        início
                    ],
                    expand=True
                )
            ],
            expand=True
        )
    )
    

ft.app(target=main)