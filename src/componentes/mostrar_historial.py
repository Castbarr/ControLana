import flet as ft
from vistas_base.base_vista_dialogos import BaseVistaDialogos
from datos.manejo_datos import ManejoDatos


class MostrarHistorial:
    def __init__(self, page, usuario, key, titulo, ):
        self.page = page
        self.usuario = usuario
        self.key = key
        self.titulo = titulo

        self.boton_cerrar = ft.Button(
            "Cerrar",
            on_click=self.cerrar_dialogo
        )

        self.movimientos = ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("Fecha")),
                ft.DataColumn(label=ft.Text("Rubro")),
                ft.DataColumn(label=ft.Text("Monto"))
            ],
            rows=[]
        )

        self.dialogo = BaseVistaDialogos(
            page,
            title=self.titulo,
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                controls=[self.movimientos],
            ),
            actions=[ft.Column([self.boton_cerrar])]
        )
        self.cargar_datos()

    def cargar_datos(self):
        if self.key == "movimientos_ingresos":
            datos = ManejoDatos.obtener_movimientos_ingresos(self.usuario)
        else:
            datos = ManejoDatos.obtener_movimientos_egresos(self.usuario)
        datos.reverse()
        if datos:
            self.movimientos.rows = [
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(fecha)),
                        ft.DataCell(ft.Text(rubro)),
                        ft.DataCell(ft.Text(str(monto))),
                    ]
                )
                for fecha, rubro, monto in (d.values() for d in datos)
            ]
        else:
            self.movimientos.rows = [
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Sin datos", color=ft.Colors.GREY_800, italic=True)),
                        ft.DataCell(ft.Text("Sin datos", color=ft.Colors.GREY_800, italic=True)),
                        ft.DataCell(ft.Text("Sin datos", color=ft.Colors.GREY_800, italic=True)),

                    ]
                )
            ]

    def cerrar_dialogo(self):
        self.dialogo.close()




