class Usuario:
    """Clase que representa una persona registrada en el sistema"""

    def __init__(self, identificacion: int, nombre: str, correo: str):
        self.identificacion = identificacion
        self.nombre = nombre.strip().capitalize()
        self.correo = correo.strip().lower()

    def mostrar_informacion(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"
