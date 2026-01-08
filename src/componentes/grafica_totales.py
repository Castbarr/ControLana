import flet as ft
import matplotlib.pyplot as plt
import flet_charts as fch
from vistas_base.base_vista_dialogos import BaseVistaDialogos

from datos.manejo_datos import ManejoDatos

class GraficaTotales:
    def __init__(self, page, usuario):
        self.page = page
        self.usuario = usuario

        self.boton_cerrar = ft.Button(
            "Cerrar",
            on_click=self.cerrar_dialogo
        )

        self.grafico = fch.MatplotlibChart(
            figure=self.crear_grafico(),
            expand=True
        )

        self.grafico.height = 500

        self.dialogo = BaseVistaDialogos(
            page,
            title=f"Datos de: {self.usuario}",
            content=self.grafico,
            actions=[self.boton_cerrar]
        )


    def crear_grafico(self):
        fig, ax = plt.subplots()
        plt.subplots_adjust(
            left=0.15,
            right=0.95,
            top=0.9,
            bottom=0.15
        )

        ingreso = ManejoDatos.obtener_ingreso_total(self.usuario)
        egreso = ManejoDatos.obtener_egreso_total(self.usuario)

        rubro = ["Ingresos", "Egresos"]
        cantidad = [ingreso, egreso]
        bar_labels = ["Ingresos", "Egresos"]
        bar_colors = ["tab:blue", "tab:red"]

        bars = ax.bar(rubro, cantidad, label=bar_labels, color=bar_colors)

        ax.bar_label(bars)
        ax.set_ylabel("Cantidad")
        ax.set_title("Totales Globales")
        ax.legend(title="Movimientos")

        return fig

    def cerrar_dialogo(self):
        self.dialogo.close()







