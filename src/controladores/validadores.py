import re

class Validador:
    """
    Valida nombre de recurso y contraseña
    """

    @staticmethod
    def validate_name(name: str, existing_names: list[str] | None = None):
        # Limpieza básica
        if not name:
            return False, "El nombre es obligatorio"

        name = name.strip()



        # Longitud
        if len(name) < 3:
            return False, "El nombre debe tener al menos 3 caracteres"

        if len(name) > 30:
            return False, "El nombre no puede exceder 30 caracteres"

        # Caracteres permitidos
        if not re.match(r"^[A-Za-z0-9 ]+$", name):
            return False, "El nombre solo puede contener letras, números y espacios"

        # Duplicados
        if existing_names and name in existing_names:
            return False, "Ya existe un recurso con ese nombre"

        return True, ""

    @staticmethod
    def validate_password(password: str):
        if not password:
            return False, "La contraseña es obligatoria"

        # Longitud
        if len(password) < 6:
            return False, "La contraseña debe tener al menos 6 caracteres"

        if len(password) > 64:
            return False, "La contraseña no puede exceder 64 caracteres"

        # Al menos una letra
        if not re.search(r"[A-Za-z]", password):
            return False, "La contraseña debe contener al menos una letra"

        # Al menos un número
        if not re.search(r"\d", password):
            return False, "La contraseña debe contener al menos un número"

        return True, ""

    @staticmethod
    def validar_cantidad(cantidad):
        # Validar cantidad vacía
        if cantidad is None:
            return False, "Debes ingresar una cantidad", None

        cantidad_str = str(cantidad).strip()
        if not cantidad_str:
            return False, "Debes ingresar una cantidad", None

        # Validar número
        try:
            monto = float(cantidad_str)
        except ValueError:
            return False, "La cantidad debe ser un número", None

        # Validar positivo
        if monto <= 0:
            return False, "La cantidad debe ser mayor a 0", None

        return True,"", monto

    @staticmethod
    def validar_rubro(rubro):
        # Validar rubro
        if not rubro:
            return False, "Debes seleccionar un rubro"
        return True, ""

    @staticmethod
    def validar_dinero_disponible(saldo, retiro):
        if retiro is None:
            return False, "Cantidad inválida"
        if saldo < retiro:
            return False, "No cuentas con saldo suficiente"
        return True, ""
