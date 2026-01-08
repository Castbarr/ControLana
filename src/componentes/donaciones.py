import flet as ft


def banner_donacion(url: str = "https://paypal.me/donacionescastbarr") -> ft.Container:

    async def open_url(e):
        await e.page.launch_url(url)

    return ft.Container(
        content=ft.Row(
            [
                ft.Text("☕ Apóyanos", size=14, weight=ft.FontWeight.BOLD),
                ft.Button(
                    "Donar",
                    icon=ft.Icons.PAYPAL,
                    on_click=open_url,
                    bgcolor=ft.Colors.BLUE_ACCENT_700,
                    color=ft.Colors.WHITE,
                    height=30,
                    tooltip="Apóyanos para seguir creando aplicaciones gratuitas",
                ),
            ],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=ft.padding.all(8),
        bgcolor=ft.Colors.RED_ACCENT_200,
        border_radius=8,
        width=230,
        margin=ft.Margin(
            top=35,
        )
    )