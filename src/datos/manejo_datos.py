import os
import json
import hashlib
from datetime import datetime
from collections import defaultdict

ARCHIVO_DATOS = "controles.json"


class ManejoDatos:
    # ──────────────────────────────
    # Storage JSON local
    # ──────────────────────────────
    @staticmethod
    def abrir_datos():
        if not os.path.exists(ARCHIVO_DATOS):
            return {}
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def guardar_datos(datos):
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    # ──────────────────────────────
    # Lógica de negocio
    # ──────────────────────────────
    @staticmethod
    def agregar_dinero(usuario, rubro, dinero):
        datos = ManejoDatos.abrir_datos()

        datos.setdefault(usuario, {})
        datos[usuario][rubro] = float(datos[usuario].get(rubro, 0)) + float(dinero)
        datos[usuario]["saldo"] = float(datos[usuario].get("saldo", 0)) + float(dinero)

        datos[usuario].setdefault("movimientos_ingresos", []).append({
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "rubro": rubro,
            "monto": float(dinero)
        })

        ManejoDatos.guardar_datos(datos)

    @staticmethod
    def disponer_dinero(usuario, rubro, dinero):
        datos = ManejoDatos.abrir_datos()

        datos.setdefault(usuario, {})
        datos[usuario][rubro] = float(datos[usuario].get(rubro, 0)) + float(dinero)
        datos[usuario]["saldo"] = float(datos[usuario].get("saldo", 0)) - float(dinero)

        datos[usuario].setdefault("movimientos_egresos", []).append({
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "rubro": rubro,
            "monto": float(dinero)
        })

        ManejoDatos.guardar_datos(datos)

    @staticmethod
    def obtener_saldo_actual(usuario):
        datos = ManejoDatos.abrir_datos()
        return datos.get(usuario, {}).get("saldo", 0.0)

    @staticmethod
    def obtener_ingreso_total(usuario):
        datos = ManejoDatos.abrir_datos()
        movimientos = datos.get(usuario, {}).get("movimientos_ingresos", [])
        lista = []
        for movimiento in movimientos:
            monto = movimiento["monto"]
            lista.append(monto)
        return sum(lista)

    @staticmethod
    def obtener_egreso_total(usuario):
        datos = ManejoDatos.abrir_datos()
        movimientos = datos.get(usuario, {}).get("movimientos_egresos", [])
        lista = []
        for movimiento in movimientos:
            monto = movimiento["monto"]
            lista.append(monto)
        return sum(lista)

    @staticmethod
    def obtener_ingreso_total_rubros(usuario):
        datos = ManejoDatos.abrir_datos()
        movimientos = datos.get(usuario, {}).get("movimientos_ingresos", [])
        totales = defaultdict(float)
        for movimiento in movimientos:
            totales[movimiento["rubro"]] += float(movimiento["monto"])
        return  totales



    @staticmethod
    def obtener_egreso_total_rubros(usuario):
        datos = ManejoDatos.abrir_datos()
        movimientos = datos.get(usuario, {}).get("movimientos_egresos", [])
        totales = defaultdict(float)
        for movimiento in movimientos:
            totales[movimiento["rubro"]] += float(movimiento["monto"])
        return totales

    @staticmethod
    def obtener_movimientos_ingresos(usuario):
        datos = ManejoDatos.abrir_datos()
        movimientos = datos.get(usuario, {}).get("movimientos_ingresos", [])
        return movimientos

    @staticmethod
    def obtener_movimientos_egresos(usuario):
        datos = ManejoDatos.abrir_datos()
        movimientos = datos.get(usuario, {}).get("movimientos_egresos", [])
        return movimientos

    @staticmethod
    def get_name_controls_low():
        datos = ManejoDatos.abrir_datos()
        lista = list(datos.keys())
        nombres = [nombre.lower() for nombre in lista]
        return nombres

    @staticmethod
    def get_name_controls_origin(self):
        datos = ManejoDatos.abrir_datos()
        return list(datos.keys())



    #--------------------SEGURIDAD------------------#

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        return ManejoDatos.hash_password(password) == hashed