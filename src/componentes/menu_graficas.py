import flet as ft
from vistas_base.base_vista_dialogos import BaseVistaDialogos

class MenuGraficas:
    def __init__(self, page: ft.Page, usuario: str):
        self.page = page
        self.usuario = usuario

        self.dialogo = BaseVistaDialogos(
            page,
            title= "Opciones de Gráficas",
            content=ft.Column(
                tight=True,
                controls=[
                    ft.Button(
                        "Totales Globales",
                        on_click=self._abrir_totales
                    ),
                    ft.Button(
                        "Totales por Rubros",
                        on_click=self._abrir_rubros
                    ),
                ]
            ),
            actions=[
                ft.TextButton("Cerrar", on_click=self.cerrar)
            ]
        )

    def mostrar(self):
        self.dialogo.open()
        self.page.update()

    def cerrar(self, e):
        self.dialogo.close()
        self.page.update()

    def _abrir_totales(self):
        self.dialogo.close()
        from componentes.grafica_totales import GraficaTotales
        GraficaTotales(self.page, self.usuario).dialogo.open()

    def _abrir_rubros(self, e):
        self.dialogo.close()
        from componentes.grafica_rubros_totales import GraficaRubrosTotales
        GraficaRubrosTotales(self.page, self.usuario).dialogo.open()