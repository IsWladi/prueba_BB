import re

class Robot():
    def vuelve(self, movimientos: str) -> bool:
        # Validaciones de error
        regex_valida_movimientos = r"^[ID]*$" # solo contiene 0 o más de cualquiera de los caracteres; "I" o "D"
        if (not isinstance(movimientos, str)) or (not re.match(regex_valida_movimientos, movimientos)):
            raise AssertionError("movimientos debe ser de tipo string y tener el patrón '^[ID]*$'")

        # Validaciones de movimientos
        if len(movimientos) == 0 :
            return True
        elif movimientos.count("I") == movimientos.count("D"):
            return True
        return False # el robot no regresó al inicio

