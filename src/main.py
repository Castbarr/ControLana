import flet as ft
from app.app import App

async def main(page: ft.Page):
    app = App(page)
    await app.start()


if __name__ == "__main__":
    ft.run(main,view=ft.AppView.WEB_BROWSER, assets_dir="assets")

