import flet as ft

from vistas_base.base_vista_dialogos import BaseVistaDialogos
from controladores.validadores import Validador
from datos.manejo_datos import ManejoDatos


class CrearControl:
    def __init__(self, page: ft.Page, enviando):
        self.page = page
        self.enviando = enviando


        #COMPONENTES

        self.name_field =  ft.TextField(
            label="Nombre del control"
        )

        self.name_error = ft.Text(
            "",
            size=12,
            color=ft.Colors.RED,
            visible=False
        )

        self.pass_field = ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
        )

        self.pass_error = ft.Text(
            "",
            size=12,
            color=ft.Colors.RED,
            visible=False
        )

        self.dialogo = BaseVistaDialogos(
            page,
            title="Crear control",
            content=ft.Column(
                tight=True,
                controls=[
                    self.name_field,
                    self.name_error,
                    self.pass_field,
                    self.pass_error,
                ]
            ),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=self.close
                ),
                ft.Button(
                    "Crear",
                    on_click=self.enviar
                )
            ]

        )

    def open(self):
        self.name_field.value = ""
        self.name_error.visible = False
        self.pass_field.value = ""
        self.pass_error.visible = False
        self.dialogo.open()

    def close(self):
        self.dialogo.close()

    def enviar(self):
        name = self.name_field.value.strip()
        password = self.pass_field.value.strip()

        if name.lower() in ManejoDatos.get_name_controls_low():
            self.name_error.value = "Ya existe un control con ese nombre"
            self.name_error.visible = True
            return

        # Validación
        ok_name, msg_name = Validador.validate_name(name)
        if not ok_name:
            self.name_error.value = msg_name
            self.name_error.visible = True
            self.pass_error.visible = False
            self.page.update()
            return  # SE DETIENE AQUÍ

        ok_pass, msg_pass = Validador.validate_password(password)
        if not ok_pass:
            self.pass_error.value = msg_pass
            self.pass_error.visible = True
            self.name_error.visible = False
            self.page.update()
            return  # SE DETIENE AQUÍ

        self.enviando(name, password)
        self.close()


