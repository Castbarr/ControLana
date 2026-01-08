import flet as ft


class VistaPrivacidad:
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
            route="/privacidad",
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
                                ft.Text(
                                    "Política de Privacidad",
                                    size=26,
                                    weight=ft.FontWeight.BOLD,
                                ),

                                self.indicador_scroll,

                                ft.Text(
                                    "ControLana es una aplicación gratuita, diseñada para el control personal de finanzas.",
                                    size=16,
                                ),

                                ft.Text(
                                    "1. Recopilación de datos",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    "La aplicación no recopila, transmite ni comparte datos personales con servidores externos. "
                                    "Toda la información se almacena únicamente de forma local en el dispositivo del usuario."
                                ),

                                ft.Text(
                                    "2. Uso de la información",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    "Los datos ingresados se utilizan exclusivamente para el funcionamiento interno de la aplicación, "
                                    "como el cálculo de saldos, generación de gráficas y de reportes."
                                ),

                                ft.Text(
                                    "3. Almacenamiento",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    "La información se guarda localmente en el dispositivo del usuario. "
                                    "No se realiza sincronización en la nube ni envío de datos a terceros."
                                ),

                                ft.Text(
                                    "4. Permisos",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    "La aplicación no solicita permisos sensibles como acceso a cámara, micrófono, ubicación o contactos."
                                ),

                                ft.Text(
                                    "5. Seguridad",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    "ControLana no accede a información fuera del ámbito de la aplicación ni realiza operaciones "
                                    "en segundo plano sin el conocimiento del usuario."
                                ),

                                ft.Text(
                                    "6. Cambios a esta política",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    "Cualquier cambio en esta política será comunicado mediante una actualización de la aplicación."
                                ),

                                ft.Divider(),

                                ft.Text(
                                    "© 2025 ControLana. Todos los derechos reservados.",
                                    size=14,
                                    italic=True,
                                    color=ft.Colors.GREY_700,
                                ),

                                ft.Button(
                                    "Volver",
                                    icon=ft.Icons.ARROW_BACK,
                                    on_click=self.volver_home
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

    def volver_home(self):
        self.app.cambio_ruta("/")

