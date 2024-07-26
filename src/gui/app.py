import flet as ft

def main(page: ft.Page):
    page.title = "Gestão de Inventário"
    page.window_min_width = 400
    page.window_min_height = 600

    navRail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        extended=True,
        min_width=100,
        min_extended_width=220,
        group_alignment=-0.6,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME, label="Início"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.INVENTORY, label="Estoque"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SELL, label="Vendas"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.FACTORY, label="Fornecedores"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SHOW_CHART, label="Relatório"
            )
        ],
        on_change=lambda e: print("Destino selecionado: ", e.control.selected_index)
    )

    page.add(
        ft.Row(
            [
                navRail,
                ft.VerticalDivider(width=1),
                ft.Column([ft.Text("Body")], alignment=ft.MainAxisAlignment.START, expand=True)
            ],
            expand=True
        )
    )

ft.app(target=main)
