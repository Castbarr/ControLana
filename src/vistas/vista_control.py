import flet as ft
from vistas_base.base_vista_dialogos import BaseVistaDialogos
from controladores.validadores import Validador
from datos.manejo_datos import ManejoDatos
from componentes.menu_graficas import MenuGraficas
from componentes.mostrar_historial import MostrarHistorial
from componentes.donaciones import banner_donacion


class VistaControl:
    def __init__(self, page: ft.Page, app):
        self.page = page
        self.app = app

        self.control = ""
        # ───── Encabezado ─────
        self.usuario = ft.Text(
            size=24,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.GREEN_300,
            style=ft.TextStyle(italic=True),
        )
        self.titulo = ft.Text(size=24, weight=ft.FontWeight.BOLD)
        self.area_titulo = ft.Row(alignment=ft.MainAxisAlignment.CENTER, wrap=True)

        self.saldo = ft.Text(size=24, weight=ft.FontWeight.BOLD)
        self.area_saldo = ft.Row(alignment=ft.MainAxisAlignment.CENTER, wrap=True)

        # ───── Ingresos ─────
        self.lista_rubros_ingresos = [
            "Salario", "Inversiones", "Préstamo solicitado", "Obsequio",
            "Préstamo reintegrado", "Premios", "Retiro de ahorro", "Otros ingresos"
        ]

        self.etiqueta_agregar = ft.Text(size=18, weight=ft.FontWeight.BOLD)

        self.lista_opciones_agregar = ft.Dropdown(
            label="Selecciona el rubro",
            options=[ft.dropdown.Option(item) for item in self.lista_rubros_ingresos],
            width=300
        )

        self.campo_agregar = ft.TextField(label="Ingresar Cantidad")

        self.boton_agregar = ft.Button(
            "Agregar",
            on_click=self.seleccion_rubro_agregar,
        )

        self.btn_hist_ingresos = ft.Button(
            "Ver ingresos",
            on_click=self.ver_historial_ingresos
        )

        # ───── Egresos ─────
        self.lista_rubros_egresos = [
            "Deudas", "Ahorro", "Electrodomésticos", "Despensa",
            "Transporte", "Recibos", "Alquiler", "Diversiones",
            "Antojos", "Ropa", "Otros gastos"
        ]

        self.etiqueta_disponer = ft.Text(size=18, weight=ft.FontWeight.BOLD)

        self.lista_opciones_disponer = ft.Dropdown(
            label="Selecciona el rubro",
            options=[ft.dropdown.Option(item) for item in self.lista_rubros_egresos],
            width=300
        )

        self.campo_disponer = ft.TextField(label="Ingresar Cantidad")

        self.boton_disponer = ft.Button(
            "Disponer",
            on_click=self.seleccion_rubro_disponer,
        )

        self.btn_hist_egresos = ft.Button(
            "Ver egresos",
            on_click=self.ver_historial_egresos
        )

        # ───── Otros ─────
        self.boton_volver = ft.Button(
            "Volver",
            icon=ft.Icons.ARROW_BACK,
            on_click=self.volver_home
        )
        self.boton_graficas = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Button(
                    "Gráficas",
                    icon=ft.Icons.BAR_CHART,
                    on_click=self.mostrar_menu_graficas
                )
            ]
        )
        self.donacion = banner_donacion()

        self.contenedor_volver_banner = ft.Row(
            [self.boton_volver, self.donacion], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,)

        # ───── AlertDialog feedback ─────
        self.dialog_text = ft.Text("", size=16)
        self.dialogo = BaseVistaDialogos(
            page,
            title="Mensaje",
            content=self.dialog_text,
            actions=[
                ft.TextButton(
                    "Aceptar",
                    on_click=self._cerrar_dialogo
                )
            ]
        )


        # ───── Layout principal ─────
        self.contenido = ft.Container(
            expand=True,
            content=ft.ResponsiveRow(
                spacing=30,
                controls=[
                    ft.Column(
                        col={"xs": 12, "sm": 6},
                        controls=[
                            self._card_seccion(
                                "Ingresos",
                                [
                                    self.etiqueta_agregar,
                                    self.lista_opciones_agregar,
                                    self.campo_agregar,
                                    self.boton_agregar,
                                    self.btn_hist_ingresos,
                                ],
                            )
                        ],
                    ),
                    ft.Column(
                        col={"xs": 12, "sm": 6},
                        controls=[
                            self._card_seccion(
                                "Egresos",
                                [
                                    self.etiqueta_disponer,
                                    self.lista_opciones_disponer,
                                    self.campo_disponer,
                                    self.boton_disponer,
                                    self.btn_hist_egresos,
                                ],
                            )
                        ],
                    ),
                ],
            ),
        )

        # ──────────────────────────────
        # Inicializar control
        # ──────────────────────────────

    def set_control(self, name):
        self.control = name
        self.usuario.value = self.control
        self.titulo.value = "Control de Gastos:"
        self.area_titulo.controls = [self.titulo, self.usuario]

        self.etiqueta_agregar.value = "Ingresar Dinero"
        self.etiqueta_disponer.value = "Disponer Dinero"

        self.lista_opciones_agregar.value = None
        self.campo_agregar.value = ""
        self.campo_agregar.on_blur = self.reset_error

        self.lista_opciones_disponer.value = None
        self.campo_disponer.value = ""
        self.campo_disponer.on_blur = self.reset_error

        self.saldo.value = f"Saldo: ${ManejoDatos.obtener_saldo_actual(name)}"
        self.area_saldo.controls = [self.saldo]
        self.page.update()

    # ──────────────────────────────
    # Vista
    # ──────────────────────────────
    def build(self):
        return ft.View(
            controls=[
                ft.Container(
                    expand=True,
                    bgcolor=ft.Colors.GREEN_300,
                    content=ft.Container(
                        expand=True,
                        margin=40,
                        padding=30,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=20,
                        content=ft.Column(
                            spacing=25,
                            scroll=ft.ScrollMode.AUTO,
                            controls=[
                                self.area_titulo,
                                ft.Divider(),
                                self.area_saldo,
                                self.contenido,
                                self.boton_graficas,
                                self.contenedor_volver_banner,
                            ],
                        ),
                    ),
                )
            ],
        )

        # ──────────────────────────────
        # Acciones
        # ──────────────────────────────
    def seleccion_rubro_agregar(self, e):
        rubro = self.lista_opciones_agregar.value
        cantidad = self.campo_agregar.value

        ok, msg = Validador.validar_rubro(rubro)
        if not ok:
            self.lista_opciones_agregar.error_text = msg
            self.page.update()
            return
        self.lista_opciones_agregar.error_text = None

        ok, msg, _ = Validador.validar_cantidad(cantidad)
        if not ok:
            self.campo_agregar.error = msg
            self.page.update()
            return
        self.campo_agregar.error= None

        ManejoDatos.agregar_dinero(self.control, rubro, cantidad)
        self.saldo.value = f"Saldo: ${ManejoDatos.obtener_saldo_actual(self.control)}"
        self.campo_agregar.value = ""
        self.lista_opciones_agregar.value= None
        self._mostrar_dialogo("Transacción exitosa")
        self.page.update()



    def seleccion_rubro_disponer(self, e):
        rubro = self.lista_opciones_disponer.value
        cantidad = self.campo_disponer.value
        saldo_actual = ManejoDatos.obtener_saldo_actual(self.control)

        ok, msg = Validador.validar_rubro(rubro)
        if not ok:
            self.lista_opciones_disponer.error_text = msg
            self.page.update()
            return
        ok, msg, _ = Validador.validar_cantidad(cantidad)
        if not ok:
            self.campo_disponer.error = msg
            self.page.update()
            return


        ok, msg = Validador.validar_dinero_disponible(
            float(saldo_actual),
            float(cantidad)
        )

        if not ok:
            self.campo_disponer.error = msg
            self.page.update()
            return

        self.lista_opciones_disponer.error_text= None
        self.campo_disponer.error= None

        ManejoDatos.disponer_dinero(self.control, rubro, cantidad)
        self.saldo.value = f"Saldo: ${ManejoDatos.obtener_saldo_actual(self.control)}"
        self.campo_disponer.value = ""
        self.lista_opciones_disponer.value = None
        self._mostrar_dialogo("Transacción exitosa")
        self.page.update()

    # ──────────────────────────────
    # Historiales y gráficas
    # ──────────────────────────────
    def ver_historial_ingresos(self, e):
         MostrarHistorial(
             page=self.page,
             usuario=self.control,
             key="movimientos_ingresos",
             titulo="Historial de Ingresos"
         ).dialogo.open()

    def ver_historial_egresos(self, e):
        MostrarHistorial(
            page=self.page,
            usuario=self.control,
            key="movimientos_egresos",
            titulo="Historial de Egresos"
        ).dialogo.open()

    def mostrar_menu_graficas(self, e):
        MenuGraficas(self.page, self.usuario.value).mostrar()

    # ──────────────────────────────
    # UI helper
    # ──────────────────────────────
    def _card_seccion(self, titulo, controles):
        return ft.Container(
            expand=True,
            padding=20,
            border_radius=15,
            bgcolor=ft.Colors.GREY_50,
            content=ft.Column(
                spacing=15,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(titulo, size=18, weight=ft.FontWeight.BOLD),
                    *controles
                ],
            ),
        )

    def _mostrar_dialogo(self, mensaje: str):
        self.dialog_text.value = mensaje
        self.dialogo.open()

    def _cerrar_dialogo(self):
        self.dialogo.close()

    def reset_error(self, e):
        # Se ejecuta al perder el foco
        self.campo_disponer.error_text = None
        self.campo_agregar.error_text = None
        self.campo_disponer.update()
        self.campo_agregar.update()

    def volver_home(self):
        self.app.cambio_ruta("/")
        self.dialogo.close()
