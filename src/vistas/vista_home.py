import flet as ft
from vistas.vista_dialog_crear_control import CrearControl
from datos.manejo_datos import ManejoDatos
from datos.admin_control import Controles
from datos.eliminar_control import EliminarControl



class VistaHome:
    def __init__(self, page: ft.Page, app):
        self.page = page
        self.app = app

        #-----------ESTADO-------------#
        self.controles = None

        self._crear_componentes()
        self.cargar_btns_controls()



        #----------COMPONENTES---------#
    def _crear_componentes(self):
        self.logo = ft.Image(
            src="logo_finanzas.png",
            width=280,
        )
        self.msg_bienvenida = ft.Text(
            "Bienvenido a Controlana",
            style=ft.TextStyle(
                size=24,
                weight=ft.FontWeight.BOLD,
                italic=True,
                letter_spacing=1.2,
                word_spacing=3,
                font_family="Arial"
            )
        )
        self.titulo_controls = ft.Text(
            "Controles",
            style=ft.TextStyle(
                size=26,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
                italic=True,
                letter_spacing=1.2,
                word_spacing=3,
                decoration=ft.TextDecoration.UNDERLINE,
                decoration_color=ft.Colors.GREEN_100,
                decoration_thickness=1,
                font_family="Arial"
            )
        )
        self.text_aviso_controls = ft.Text(
            "No has creado ningún Control",
            style=ft.TextStyle(
                size=12,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.GREY_800,
                letter_spacing=1.2,
                word_spacing=3,
                font_family="Arial"
            )
        )
        self.btns_list_controls = ft.Row(
            spacing=12,
            alignment=ft.MainAxisAlignment.CENTER,
            wrap=True,
        )
        self.contenedor_btns_controls = ft.Container(
            content=ft.Column(
                height=100,
                scroll=ft.ScrollMode.AUTO,
                controls=[self.text_aviso_controls,self.btns_list_controls]
            )
        )
        self.btn_add_control = ft.IconButton(
            icon=ft.Icons.ADD,
            icon_size=32,
            icon_color=ft.Colors.GREEN_800,
            bgcolor=ft.Colors.AMBER_200,
            tooltip="Crear control",
            on_click=self.crear_control,
        )
        self.btn_del_control = ft.IconButton(
            icon=ft.Icons.REMOVE,
            icon_size=32,
            icon_color=ft.Colors.GREEN_800,
            bgcolor=ft.Colors.AMBER_200,
            tooltip="Eliminar control",
            on_click=self.eliminar_control,
        )
        self.btns_add_del_controls = ft.Row(
            controls=[
                self.btn_add_control,
                self.btn_del_control
            ],
            spacing=42,
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.btn_info = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.TextButton(
                    "Política de privacidad",
                    icon=ft.Icons.INFO_OUTLINE,
                    on_click=self.ir_privacidad
                ),
                ft.Button(
                    "Acerca de",
                    icon=ft.Icons.INFO,
                    bgcolor=ft.Colors.GREEN_100,
                    color=ft.Colors.GREEN_900,
                    on_click=self.ir_acerca,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=12),
                        elevation=0,
                        padding=ft.Padding.symmetric(horizontal=20, vertical=12),
                    )
                )
            ]
        )
        self.contenedor_btn_info = ft.Container(
            content=self.btn_info,
        )



    def build(self):
        return ft.View(
            controls=[
                ft.Container(
                    expand=True,
                    bgcolor=ft.Colors.GREEN_300,
                    content=ft.Container(
                        expand=True,
                        margin=40,
                        padding=20,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=20,
                        content=ft.Column(
                            spacing=18,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                self.contenedor_btn_info,
                                self.logo,
                                self.msg_bienvenida,
                                ft.Divider(height=20),
                                self.titulo_controls,
                                self.contenedor_btns_controls,
                                self.btns_add_del_controls,
                            ],
                        ),
                    ),
                )
            ],
        )

    def crear_control(self):
        """Se recaban el name y password se pasan a la funcion admin_control
        para continuar el proceso de crear control"""
        CrearControl(self.page,enviando=self.admin_control).open()

    def admin_control(self, name, password):
        """Se hashea el password, se guardan los datos de control y
        se crea el boton"""
        hashed_password = ManejoDatos.hash_password(password)
        Controles.agregar_control(name, hashed_password)
        self.crear_btn_control(name)

    def crear_btn_control(self, name):
        """Se crea el boton para los controles"""
        boton = ft.Button(
            name,
            icon=ft.Icon(ft.Icons.ACCOUNT_BALANCE_WALLET),
            height=45,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
                padding=ft.Padding.symmetric(horizontal=20),
            ),
            on_click=self.abrir_control
        )
        self.text_aviso_controls.visible =False
        self.btns_list_controls.controls.append(boton)

    def abrir_control(self, e):
        self.app.name_control = e.control.content
        self.app.cambio_ruta("/control_acceso")

    def cargar_btns_controls(self):
        self.btns_list_controls.controls.clear()
        for name in Controles.cargar_control():
            self.crear_btn_control(name)

    def eliminar_control(self, e):
        self.controles = ManejoDatos.abrir_datos()
        EliminarControl(
            self.page,
            controles=self.controles.keys(),
            on_confirm=self.confirmar_eliminacion
        ).open()

    def confirmar_eliminacion(self, name):
        for control in self.controles:
            if control == name:
                del self.controles[control]
                Controles.eliminar_control(name)
                if not self.controles:
                    self.text_aviso_controls.visible = True
                self.recargar_controles()
                return True, ""
        return False, "Control no existe"

    def recargar_controles(self):
        self.btns_list_controls.controls.clear()
        for control in self.controles:
            self.crear_btn_control(control)
        self.page.update()

    def ir_acerca(self):
        self.app.cambio_ruta("/acerca")

    def ir_privacidad(self):
        self.app.cambio_ruta("/privacidad")











