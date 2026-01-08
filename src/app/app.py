import flet as ft
from vistas.vista_home import VistaHome
from controladores.control_acceso import ControlAcceso
from vistas.vista_control import VistaControl
from componentes.acerca_de import VistaAcerca
from componentes.privacidad import VistaPrivacidad


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.name_control = ""
        self.acerca_de = VistaAcerca(self.page, self)
        self.home = VistaHome(self.page, self)
        self.control_acceso =ControlAcceso(self.page, self)
        self.privacidad = VistaPrivacidad(self.page, self)
        self.vista_control = VistaControl(self.page, self)



        self.ruta = ""

    async def start(self):
        await self.config_pagina()
        self.iniciar()

    async def config_pagina(self):
        self.page.title = "ControLana"
        self.page.window.icon = "favicon.ico"
        self.page.window.resizable = False
        self.page.window.height = 850
        self.page.window.width = 700
        self.page.add(self.splash())
        await self.page.window.center()
        self.page.update()


    def iniciar(self):
        self.page.views.clear()
        self.page.views.append(self.home.build())
        self.page.update()

    def cambio_ruta(self, ruta):
        self.ruta = ruta
        self.page.views.clear()
        if self.ruta == "/":
            self.page.views.append(self.home.build())
        elif self.ruta == "/control_acceso":
            self.page.views.append(self.control_acceso.build())
        elif self.ruta == "/control":
            self.page.views.append(self.vista_control.build())
        elif self.ruta == "/acerca":
            self.page.views.append(self.acerca_de.build())
        elif self.ruta == "/privacidad":
            self.page.views.append(self.privacidad.build())
        self.page.update()

    def splash(self):
        return ft.Container(
            expand=True,
            alignment=ft.Alignment.CENTER,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.ProgressRing(),
                    ft.Text("Iniciando aplicación...")
                ]
            )
        )













