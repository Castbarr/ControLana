import flet as ft
from vistas_base.base_vista_dialogos import BaseVistaDialogos
from datos.admin_control import Controles
from datos.manejo_datos import ManejoDatos
from componentes.donaciones import banner_donacion



class ControlAcceso:
    def __init__(self, page: ft.Page, app):
        self.page = page
        self.app = app

        self.password = ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
            width=300,
        )

        self.error = ft.Text(
            "",
            color=ft.Colors.RED,
            visible=False
        )

        self.vista_password = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[self.password],
        )

        self.dialogo = BaseVistaDialogos(
            page,
            title="Contraseña olvidada",
            content = ft.Text(
                "Por seguridad, no es posible recuperar la contraseña.\n\n"
                "Puedes eliminar este Control en la pantalla principal.\n"
                "Eso borrara todos sus datos almacenados localmente."
            ),
            actions = [
                ft.TextButton(
                    "Cancelar",
                    on_click=self.close
                ),
                ft.Button(
                    "Ir a Home",
                    on_click=self.volver_home
                )
            ]

        )

    def close(self):
        self.dialogo.close()

    def volver_home(self):
        self.app.cambio_ruta("/")
        self.dialogo.close()

    def build(self):
        return ft.View(
            controls=[
                ft.Container(
                    expand=True,
                    bgcolor=ft.Colors.GREEN_300,
                    content=ft.Container(
                        expand=True,
                        margin=ft.margin.all(40),
                        padding=30,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=20,
                        content=ft.Column(
                            spacing=20,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    "Acceso al Control",
                                    size=26,
                                    weight=ft.FontWeight.BOLD,
                                ),

                                self.vista_password,
                                self.error,

                                ft.Button(
                                    "Ingresar",
                                    icon=ft.Icons.LOCK_OPEN,
                                    on_click=self.validar,
                                    width=200,
                                ),

                                ft.TextButton(
                                    "¿Olvidaste tu contraseña?",
                                    on_click=self.mostrar_dialogo,
                                ),

                                ft.TextButton(
                                    "Cancelar",
                                    icon=ft.Icons.ARROW_BACK,
                                    on_click=lambda e: self.app.cambio_ruta("/"),
                                ),
                                ft.Row([banner_donacion()], alignment=ft.MainAxisAlignment.CENTER),
                            ],
                        ),

                    ),
                ),
            ],
        )

    def mostrar_dialogo(self):
        self.dialogo.open()

    def validar(self, e):
        name = self.app.name_control
        controles = Controles.cargar_control()
        control = controles[name]


        if control is None:
            self.app.cambio_ruta("/")
            return

        if not ManejoDatos.verify_password(
                self.password.value.strip(),
                control["password"]
        ):
            self.error.value = "Contraseña incorrecta"
            self.error.visible = True
            self.password.value = ""
            self.page.update()
            return

        self.password.value = ""
        self.error.visible = False
        self.app.vista_control.set_control(name)
        self.app.cambio_ruta("/control")




