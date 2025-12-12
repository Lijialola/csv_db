
class EmptyColumnNameError(Exception):
    def __init__(self):
        super().__init__("No se permiten textos vacíos como nombres de columnas")


class DuplicateColumnsError(Exception):
    def __init__(self):
        super().__init__("No se permiten columnas con el mismo nombre")

class NotANumberError(Exception):
    def __init__(self):
        super().__init__("Solo se permite un numero")


class NotFoundItemError(Exception):
    def __init__(self):
        super().__init__("No se ha encontrado el elemento")