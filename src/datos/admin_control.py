import json
import os

DATA_FILE = "controles.json"

class Controles:

    @staticmethod
    def cargar_control() -> dict:
        if not os.path.exists(DATA_FILE):
            return {}

        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def guardar_controles(controles: dict):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(controles, f, indent=4)

    @staticmethod
    def agregar_control(name: str, password_hash: str):
        controles = Controles.cargar_control()
        controles[name] = {
            "password": password_hash
        }
        Controles.guardar_controles(controles)

    @staticmethod
    def eliminar_control(name: str):
        controles = Controles.cargar_control()
        if name in controles:
            del controles[name]
            Controles.guardar_controles(controles)