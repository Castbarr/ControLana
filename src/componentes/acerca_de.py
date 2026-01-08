import flet as ft


class VistaAcerca:
    def __init__(self, page, app):
        self.page = page
        self.app = app

        self.indicador_scroll = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Icon(
                    ft.Icons.KEYBOARD_ARROW_DOWN,
                    size=18,
                    color=ft.Colors.GREY_500
                ),
                ft.Text(
                    "Desplázate para leer todo",
                    size=12,
                    color=ft.Colors.GREY_600,
                    italic=True
                ),
            ]
        )

    def build(self):
        return ft.View(
            controls=[
                ft.Container(
                    expand=True,
                    bgcolor=ft.Colors.GREEN_300,
                    padding=20,
                    content=ft.Container(
                        expand=True,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=20,
                        padding=30,
                        content=ft.Column(
                            spacing=20,
                            scroll=ft.ScrollMode.AUTO,
                            on_scroll=lambda e: self._on_scroll(e),
                            controls=[

                                # 🟢 TÍTULO
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Icon(ft.Icons.INFO, size=30, color=ft.Colors.GREEN_700),
                                        ft.Text(
                                            "Acerca de ControLana",
                                            size=26,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ],
                                ),

                                # 📱 DESCRIPCIÓN
                                ft.Text(
                                    "ControLana es una aplicación gratuita diseñada para ayudarte a "
                                    "llevar un control claro y sencillo de tus finanzas personales.",
                                    size=16,
                                    text_align=ft.TextAlign.CENTER,
                                ),

                                ft.Divider(),
                                self.indicador_scroll,

                                # 🔢 VERSIÓN
                                ft.Row(
                                    spacing=10,
                                    controls=[
                                        ft.Icon(ft.Icons.NEW_RELEASES_OUTLINED),
                                        ft.Text("Versión:", weight=ft.FontWeight.BOLD),
                                        ft.Text("1.0.0"),
                                    ],
                                ),

                                # ⭐ FUNCIONES
                                ft.Text(
                                    "Funciones principales",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Column(
                                    spacing=8,
                                    controls=[
                                        ft.Text("• Registro de ingresos y egresos"),
                                        ft.Text("• Organización por rubros"),
                                        ft.Text("• Visualización de saldo"),
                                        ft.Text("• Gráficas estadísticas"),
                                    ],
                                ),

                                # 🧭 MINI GUÍA
                                ft.Text(
                                    "Cómo usar la aplicación",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Column(
                                    spacing=8,
                                    controls=[
                                        ft.Text("1. Agrega tus ingresos o egresos desde la vista de control."),
                                        ft.Text("2. Consulta tu saldo actualizado en todo momento."),
                                        ft.Text("4. Visualiza el detalle de todos tus movimientos."),
                                        ft.Text("3. Visualiza tus movimientos con gráficas."),
                                    ],
                                ),

                                ft.Divider(),

                                # 🔒 PRIVACIDAD
                                ft.Row(
                                    spacing=10,
                                    controls=[
                                        ft.Icon(ft.Icons.SECURITY),
                                        ft.Text(
                                            "Tu información se almacena únicamente en tu dispositivo.",
                                            italic=True,
                                        ),
                                    ],
                                ),

                                ft.TextButton(
                                    "Ver política de privacidad",
                                    icon=ft.Icons.LOCK_OUTLINE,
                                    on_click=self.ir_privacidad
                                ),

                                ft.Divider(),

                                # 👤 CRÉDITOS
                                ft.Text(
                                    "Desarrollado por",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    "Juan Pablo Castillo 'CASTBARR' · 2026",
                                    italic=True,
                                ),

                                # ⬅ VOLVER
                                ft.Button(
                                    "Volver",
                                    icon=ft.Icons.ARROW_BACK,
                                    on_click=self.ir_home,
                                ),
                            ],
                        ),
                    ),
                )
            ],
        )

    def _on_scroll(self, e):
        # Si el usuario ya desplazó, ocultamos el indicador
        if e.pixels > 0 and self.indicador_scroll.visible:
            self.indicador_scroll.visible = False
            self.page.update()

        # (Opcional) si vuelve arriba, mostrarlo otra vez
        elif e.pixels == 0 and not self.indicador_scroll.visible:
            self.indicador_scroll.visible = True
            self.page.update()

    def ir_privacidad(self):
        self.app.cambio_ruta("/privacidad")

    def ir_home(self):
        self.app.cambio_ruta("/")
