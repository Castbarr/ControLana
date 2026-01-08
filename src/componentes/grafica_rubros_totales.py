import flet as ft
import matplotlib.pyplot as plt
import flet_charts as fch
from vistas_base.base_vista_dialogos import BaseVistaDialogos

from datos.manejo_datos import ManejoDatos

class GraficaRubrosTotales:
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
        plt.xticks(rotation=45, ha="right")
        ax.tick_params(axis="x", labelsize=8)
        ax.tick_params(axis="y", labelsize=8)
        plt.subplots_adjust(
            left=0.15,
            right=0.95,
            top=0.9,
            bottom=0.2
        )

        ingreso = ManejoDatos.obtener_ingreso_total_rubros(self.usuario)
        egreso = ManejoDatos.obtener_egreso_total_rubros(self.usuario)

        lista_rubros_ingreso = list(ingreso.keys())
        lista_rubros_egreso = list(egreso.keys())


        lista_cantidades_ingreso = list(ingreso.values())
        lista_cantidades_egreso = list(egreso.values())

        bar_ingresos = ax.bar(
            lista_rubros_ingreso,
            lista_cantidades_ingreso,
            color="tab:blue",
            label="Ingresos",
        )
        bar_egresos = ax.bar(
            lista_rubros_egreso,
            lista_cantidades_egreso,
            color="tab:red",
            label="Egresos",
        )

        labels_ingresos = ax.bar_label(bar_ingresos, padding=3)
        for label in labels_ingresos:
            label.set_rotation(45)
            label.set_fontsize(8)

        labels_egresos = ax.bar_label(bar_egresos, padding=3)
        for label in labels_egresos:
            label.set_rotation(45)
            label.set_fontsize(8)

        ax.set_ylabel("Cantidad")
        ax.set_title("Totales por Rubros")
        ax.legend(title="Movimientos")

        return fig

    def cerrar_dialogo(self):
        self.dialogo.close()