import flet as ft
from vistas_base.base_vista_dialogos import BaseVistaDialogos


class EliminarControl:
    def __init__(self, page: ft.Page, controles: list, on_confirm):
        self.page = page
        self.controles = controles
        self.on_confirm = on_confirm

        # Dropdown con controles existentes
        self.control_selector = ft.Dropdown(
            label="Selecciona el control a eliminar",
            options=[ft.dropdown.Option(c) for c in self.controles],
            width=300
        )

        self.error_text = ft.Text(
            "",
            color=ft.Colors.RED,
            size=12,
            visible=False
        )

        self.dialogo = BaseVistaDialogos(
            page,
            title="Confirmar eliminación",
            content=ft.Column(
                tight=True,
                controls=[
                    ft.Text(
                        "Esta acción eliminará el control seleccionado y "
                        "todos sus datos asociados.\n\n¿Deseas continuar?",
                        size=14
                    ),
                    self.control_selector,
                    self.error_text
                ]
            ),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=self._close
                ),
                ft.Button(
                    "Eliminar",
                    icon=ft.Icons.DELETE,
                    bgcolor=ft.Colors.RED_600,
                    color=ft.Colors.WHITE,
                    on_click=self._submit
                )
            ],
        )

    # 🔓 Abrir diálogo
    def open(self):
        self.error_text.visible = False
        self.control_selector.value = None
        self.dialogo.open()

    # ❌ Cerrar diálogo
    def _close(self, e):
        self.dialogo.close()

    # ✅ Confirmar eliminación
    def _submit(self, e):
        name = self.control_selector.value

        if not name:
            self.error_text.value = "Selecciona un control"
            self.error_text.visible = True
            self.page.update()
            return

        # Callback hacia HomeView
        ok, msg = self.on_confirm(name)

        if not ok:
            self.error_text.value = msg
            self.error_text.visible = True
            self.page.update()
            return

        self._close(e)