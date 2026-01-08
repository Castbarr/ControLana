import flet as ft


class BaseVistaDialogos:
    def __init__(
        self,
        page: ft.Page,
        title: str,
        content: ft.Control,
        actions: list[ft.Control] | None = None,
        modal: bool = True,
        width: int | None = 600,
    ):
        self.page = page

        self.dialog = ft.AlertDialog(
            modal=modal,
            title=ft.Text(title),
            content=content,
            actions=actions or [],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )

        if width:
            self.dialog.content = ft.Container(
                width=width,
                content=content
            )
        self.page.overlay.append(self.dialog)

    def open(self):
        self.page.dialog = self.dialog
        self.dialog.open = True
        self.page.update()

    def close(self):
        self.dialog.open = False
        self.page.update()

